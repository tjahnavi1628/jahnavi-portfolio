from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from pathlib import Path
from django.conf import settings
from .models import ContactMessage

def home(request):
    return render(request, "portfolio/index.html")

@require_POST
def contact(request):
    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    subject = request.POST.get("subject", "").strip()
    message = request.POST.get("message", "").strip()

    if not all([name, email, subject, message]):
        messages.error(request, "Please complete every field.")
        return redirect("/#contact")
    if len(name) > 100 or len(subject) > 200:
        messages.error(request, "Name or subject is too long.")
        return redirect("/#contact")

    try:
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
    except Exception:
        messages.error(request, "Your message could not be saved. Please try again.")
        return redirect("/#contact")

    messages.success(request, "Thank you! Your message has been submitted successfully.")
    return redirect("/#contact")

def download_resume(request):
    resume_path = Path(settings.BASE_DIR) / "static" / "files" / "resume.pdf"
    if not resume_path.is_file():
        raise Http404("Resume file is not available.")
    return FileResponse(
        open(resume_path, "rb"),
        as_attachment=True,
        filename="Jahnavi_Tiruveedula_Resume.pdf",
        content_type="application/pdf",
    )
