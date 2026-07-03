@echo off
REM Setup script for Sheozy e-commerce platform (Windows)

echo ================================
echo Sheozy E-Commerce Setup
echo ================================
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create .env file
echo Creating .env file...
if not exist .env (
    copy .env.example .env
    echo .env file created. Please update it with your configuration.
)

REM Run migrations
echo Running migrations...
python manage.py makemigrations
python manage.py migrate

REM Create superuser
echo Creating superuser...
python manage.py createsuperuser

REM Load sample data
echo Loading sample data...
python manage.py load_sample_data

REM Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput

echo.
echo ================================
echo Setup Complete!
echo ================================
echo.
echo To start the development server, run:
echo   python manage.py runserver
echo.
echo Admin panel: http://127.0.0.1:8000/admin/
echo Website: http://127.0.0.1:8000/
echo.
pause
