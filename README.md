# Sheozy - Modern E-Commerce Platform

A modern, stylish online shopping platform built with Django featuring:

- **Modern UI/UX**: Beautiful, responsive design with smooth animations
- **User Authentication**: Email/password registration and login with Google OAuth integration
- **Product Management**: Browse products by category, search, and filter
- **Shopping Cart**: Add/remove items, manage quantities
- **Checkout System**: Complete order process with shipping information
- **User Profiles**: Manage personal information and view order history
- **Admin Panel**: Manage products, categories, users, and orders

## Features

✨ **Modern Design** - Beautiful gradient colors, smooth animations, and responsive layout
🔐 **Secure Authentication** - Email/password and Google OAuth login
🛍️ **Shopping Experience** - Product browsing, filtering, search, and cart management
📦 **Order Management** - Complete checkout process and order tracking
👤 **User Profiles** - Manage user information and order history
💳 **Multiple Payment Methods** - Ready for credit card and PayPal integration

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
```bash
# Copy and update the .env file
cp .env.example .env
```

Edit `.env` with your settings:
- Change `SECRET_KEY` to a secure key
- Add Google OAuth credentials (optional)
- Configure email settings (optional)

### 4. Initialize Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Access the application at: `http://127.0.0.1:8000/`

## Admin Panel
- URL: `http://127.0.0.1:8000/admin/`
- Use superuser credentials created in step 5

## Project Structure

```
sheozy/
├── config/                 # Django configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── users/                 # User management app
│   ├── models.py          # Custom user model
│   ├── views.py           # User views
│   └── urls.py            # User URLs
├── products/              # Products app
│   ├── models.py          # Product models
│   ├── views.py           # Product views
│   └── urls.py            # Product URLs
├── cart/                  # Shopping cart app
│   ├── models.py          # Cart models
│   ├── views.py           # Cart views
│   └── urls.py            # Cart URLs
├── orders/                # Orders app
│   ├── models.py          # Order models
│   ├── views.py           # Order views
│   └── urls.py            # Order URLs
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── products/          # Product templates
│   ├── cart/              # Cart templates
│   └── orders/            # Order templates
├── static/                # Static files
│   ├── css/               # Stylesheets
│   └── js/                # JavaScript files
├── manage.py              # Django management
└── requirements.txt       # Python dependencies
```

## Authentication Setup

### Email/Password Registration
- Automatically enabled with django-allauth
- Users can register with email and password

### Google OAuth Setup
1. Create Google OAuth credentials at [Google Cloud Console](https://console.cloud.google.com/)
2. Add credentials to `.env` file
3. Configure in Django admin under "Social applications"

## Key Models

### CustomUser
Extended user model with:
- Email authentication
- Phone number
- Avatar/Profile picture
- Address information
- Verification status

### Product
- Name, description, pricing
- Stock management
- Discount prices
- Rating and reviews

### Cart & CartItem
- User/session-based shopping cart
- Item quantity management

### Order
- Order tracking
- Shipping information
- Payment status
- Order history

## Customization

### Adding Products
1. Go to admin panel (`/admin/`)
2. Navigate to Products
3. Create new products with images, pricing, and descriptions

### Styling
- Main styles: `static/css/style.css`
- All animations and responsive design included
- Customize colors in CSS root variables

### Templates
- Base template: `templates/base.html`
- Extend for custom pages using Django template inheritance

## Payment Integration (Future)

Ready for payment gateway integration:
- Stripe
- PayPal
- Square

Configure in `orders/views.py` checkout process

## Performance Features

- Lazy image loading support
- Optimized CSS with variables
- Responsive grid layouts
- Smooth animations and transitions
- Static file optimization

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Security Features

- CSRF protection
- SQL injection prevention
- Secure password hashing
- Session security
- Email validation

## Future Enhancements

- Payment gateway integration
- Advanced product filtering
- Product recommendations
- Wishlist functionality
- Product reviews and ratings
- Email notifications
- SMS notifications
- Analytics dashboard
- Inventory management
- Multi-currency support

## Support & Documentation

For more information:
- [Django Documentation](https://docs.djangoproject.com/)
- [django-allauth Documentation](https://django-allauth.readthedocs.io/)

## License

This project is open source and available for personal and commercial use.

---

**Made with ❤️ - Sheozy E-Commerce Platform**
