#!/bin/bash
# Setup script for Sheozy e-commerce platform

echo "================================"
echo "Sheozy E-Commerce Setup"
echo "================================"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/Scripts/activate 2>/dev/null || source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file
echo "Creating .env file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo ".env file created. Please update it with your configuration."
fi

# Run migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "Creating superuser..."
python manage.py createsuperuser

# Load sample data
echo "Loading sample data..."
python manage.py load_sample_data

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "To start the development server, run:"
echo "  python manage.py runserver"
echo ""
echo "Admin panel: http://127.0.0.1:8000/admin/"
echo "Website: http://127.0.0.1:8000/"
