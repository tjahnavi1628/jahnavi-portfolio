@echo off
cd /d "%~dp0"
echo Installing required packages...
python -m pip install -r requirements.txt
if errorlevel 1 (
  echo.
  echo Installation failed. Check that Python is installed and available in PATH.
  pause
  exit /b 1
)
echo.
echo Applying database migrations...
python manage.py makemigrations portfolio
python manage.py migrate
echo.
echo Starting Career Portfolio...
python manage.py runserver
pause
