# Complete Setup Guide for Sheozy E-Commerce Platform

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment support
- Git (optional)

## Installation Steps

### Step 1: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Environment Configuration

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` with your settings:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 4: Database Setup

Initialize the database with migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Admin User (Superuser)

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter:
- Username (or email if using custom user)
- Email
- Password
- Password confirmation

### Step 6: Load Sample Data (Optional)

Populate the database with sample products and categories:

```bash
python manage.py load_sample_data
```

This creates:
- 4 sample categories
- 8 sample products
- Discount pricing examples

### Step 7: Collect Static Files

Prepare static files (CSS, JavaScript, images) for serving:

```bash
python manage.py collectstatic --noinput
```

### Step 8: Start Development Server

Run the Django development server:

```bash
python manage.py runserver
```

The application will be available at:
- Website: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## Quick Setup (Automated)

### Windows Users
Run the setup batch script:
```bash
setup.bat
```

### macOS/Linux Users
Run the setup shell script:
```bash
chmod +x setup.sh
./setup.sh
```

## Google OAuth Setup (Optional)

### 1. Get Google OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Google+ API
4. Create OAuth 2.0 credentials (Web application)
5. Set authorized redirect URIs:
   - `http://localhost:8000/accounts/google/login/callback/`
   - `http://yourdomain.com/accounts/google/login/callback/`

### 2. Configure in Django Admin

1. Go to `http://127.0.0.1:8000/admin/`
2. Navigate to "Social applications"
3. Click "Add Social application"
4. Fill in:
   - Provider: Google
   - Name: Google
   - Client id: [Your Google Client ID]
   - Secret key: [Your Google Secret Key]
   - Sites: Select your site

## File Structure

```
sheozy/
├── config/                    # Django configuration
│   ├── settings.py           # Main settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI app
│   └── asgi.py               # ASGI app
├── users/                    # User management
│   ├── models.py             # CustomUser model
│   ├── views.py              # User views
│   ├── admin.py              # Admin configuration
│   └── urls.py               # User routes
├── products/                 # Product catalog
│   ├── models.py             # Product models
│   ├── views.py              # Product views
│   ├── admin.py              # Admin configuration
│   └── management/           # Management commands
├── cart/                     # Shopping cart
│   ├── models.py             # Cart models
│   ├── views.py              # Cart operations
│   └── urls.py               # Cart routes
├── orders/                   # Order management
│   ├── models.py             # Order models
│   ├── views.py              # Order views
│   └── urls.py               # Order routes
├── templates/                # HTML templates
│   ├── base.html             # Base template
│   ├── products/             # Product pages
│   ├── cart/                 # Cart pages
│   └── orders/               # Order pages
├── static/                   # Static files
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript
│   └── images/               # Images
├── manage.py                 # Django CLI
├── requirements.txt          # Dependencies
├── README.md                 # Project README
├── setup.sh                  # Linux/Mac setup
└── setup.bat                 # Windows setup
```

## Key Features Walkthrough

### 1. User Registration & Login

**Email/Password Registration:**
- Visit `/accounts/signup/`
- Enter email and password
- Verify email (if configured)

**Google OAuth:**
- Click "Sign up with Google"
- Authorize the application
- Account created automatically

### 2. Product Browsing

- Homepage displays featured products
- Filter by category
- Search functionality
- Product ratings and reviews

### 3. Shopping Cart

- Add products to cart
- Adjust quantities
- View cart total
- Cart persists for logged-in users
- Session-based cart for anonymous users

### 4. Checkout Process

- Enter shipping information
- Select payment method
- Review order
- Confirm purchase

### 5. Order Management

- View order history
- Track order status
- Download invoices (if configured)

### 6. User Profile

- View account information
- Edit profile details
- Update shipping address
- Upload profile picture

## Admin Panel Usage

### Manage Products

1. Go to `/admin/`
2. Navigate to "Products"
3. Add new product with:
   - Name and description
   - Pricing (regular and discount)
   - Stock quantity
   - Product images
   - Category assignment

### Manage Categories

1. Go to `Products → Categories`
2. Create new categories
3. Add category description and image

### Manage Users

1. Go to `Users → Users`
2. View user information
3. Edit user details
4. Manage user permissions

### View Orders

1. Go to `Orders → Orders`
2. View all orders
3. Update order status
4. View order details and items

## Customization

### Change Theme Colors

Edit `static/css/style.css`:
```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #ec4899;
    /* ... other colors ... */
}
```

### Add Custom Pages

1. Create template: `templates/pages/custom.html`
2. Create view in appropriate app
3. Add URL route in `urls.py`
4. Link from navigation

### Modify Product Fields

1. Edit `products/models.py`
2. Add new fields to Product model
3. Create migration: `python manage.py makemigrations`
4. Apply migration: `python manage.py migrate`
5. Update admin display in `products/admin.py`

## Troubleshooting

### Database Errors
```bash
# Reset database (delete all data)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py load_sample_data
```

### Static Files Not Loading
```bash
# Regenerate static files
python manage.py collectstatic --clear --noinput
```

### Port Already in Use
```bash
# Use different port
python manage.py runserver 8001
```

### Module Not Found
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## Production Deployment

### Before Going Live

1. Set `DEBUG=False` in `.env`
2. Generate strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Set up email backend for emails
5. Configure static file serving
6. Set up database (PostgreSQL recommended)
7. Enable HTTPS
8. Configure CSRF and security settings

### Recommended Hosting

- Heroku
- DigitalOcean
- AWS
- PythonAnywhere
- Render

## Support & Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [django-allauth Docs](https://django-allauth.readthedocs.io/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## Next Steps

1. ✅ Complete setup
2. ✅ Load sample data
3. ✅ Access admin panel
4. ✅ Browse website
5. ✅ Test user registration
6. ✅ Test shopping cart
7. ✅ Test checkout
8. ✅ Customize for your brand
9. ✅ Deploy to production

---

**Happy Selling with Sheozy!** 🛍️
