JAHNAVI TIRUVEEDULA - DJANGO PORTFOLIO
=====================================

QUICK START (Windows / VS Code)
1. Extract this ZIP into a folder.
2. Open that extracted folder in VS Code (the folder that contains manage.py).
3. Open Terminal -> New Terminal.
4. If you already use a virtual environment, activate it. Example:
   .\venv\Scripts\Activate.ps1
5. Run:
   python -m pip install -r requirements.txt
   python manage.py check
   python manage.py migrate
   python manage.py runserver
6. Open http://127.0.0.1:8000/

Or double-click START_PORTFOLIO.bat from the extracted folder.

PROJECT CONTENTS
- Django backend with contact form saved in SQLite
- Responsive single-page HTML/CSS/vanilla JS portfolio
- Orange + black theme
- Home, About Me, Projects, Skills, Education, Contact
- Smooth scrolling, mobile navigation, scroll progress, reveal animations
- Resume PDF download endpoint
- Admin panel for viewing contact messages

KNOWN PERSONAL LINKS
- GitHub: https://github.com/tjahnavi1628

IMPORTANT PERSONAL ASSETS
- This project runs without a photo and displays a designed initials avatar.
- To use your own photo, save it as static/images/profile.jpg.
- The included resume.pdf is a starter resume generated only from known details. Review it and replace it with your final resume PDF if needed.
- Your exact email and LinkedIn URL were not available in the conversation context I could retrieve, so they are not fabricated. The portfolio contact form works without them and saves messages to the database.
- For contact form messages: create an admin account with `python manage.py createsuperuser`, then visit http://127.0.0.1:8000/admin/

This is for local development. Before public deployment, configure production settings, secret key, allowed hosts, HTTPS, and email delivery.
