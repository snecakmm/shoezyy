# 🛍️ Sheozy - Quick Start Guide

## Get Started in 5 Minutes

### For Windows Users:

1. **Open Command Prompt** and navigate to the project folder
2. **Run the setup script:**
   ```bash
   setup.bat
   ```
3. **Follow the prompts** to create admin account
4. **Start the server:**
   ```bash
   python manage.py runserver
   ```
5. **Visit:** `http://127.0.0.1:8000/`

### For macOS/Linux Users:

1. **Open Terminal** and navigate to the project folder
2. **Run the setup script:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
3. **Follow the prompts** to create admin account
4. **Start the server:**
   ```bash
   python manage.py runserver
   ```
5. **Visit:** `http://127.0.0.1:8000/`

### Manual Setup (All Platforms):

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment file
cp .env.example .env

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create admin account
python manage.py createsuperuser

# 7. Load sample products
python manage.py load_sample_data

# 8. Collect static files
python manage.py collectstatic --noinput

# 9. Start development server
python manage.py runserver
```

## URLs to Visit

| URL | Purpose |
|-----|---------|
| `http://127.0.0.1:8000/` | Home page |
| `http://127.0.0.1:8000/products/` | All products |
| `http://127.0.0.1:8000/admin/` | Admin panel |
| `http://127.0.0.1:8000/accounts/signup/` | User registration |
| `http://127.0.0.1:8000/accounts/login/` | User login |
| `http://127.0.0.1:8000/cart/` | Shopping cart |
| `http://127.0.0.1:8000/orders/checkout/` | Checkout |

## First Steps

### 1. Explore Admin Panel
- Login at `/admin/` with your superuser account
- Create products in the Products section
- Create categories in the Categories section
- View users and orders

### 2. Browse Products
- Visit homepage to see featured products
- Click on products to view details
- Add items to cart

### 3. Test User Features
- Register a new account
- Login/logout
- View profile
- Edit profile information

### 4. Test Shopping
- Add items to cart
- Update quantities
- Proceed to checkout
- Complete order

## Features Available

✅ **User Authentication**
- Email/password registration & login
- Google OAuth (setup required)
- User profiles with avatars
- Order history

✅ **Product Catalog**
- Browse products by category
- Search functionality
- Product ratings and reviews
- Discount pricing display
- Multiple product images

✅ **Shopping Cart**
- Add/remove items
- Update quantities
- Persistent cart for logged-in users
- Real-time total calculation

✅ **Checkout & Orders**
- Complete checkout process
- Shipping information collection
- Order tracking
- Order history management

✅ **Modern Design**
- Smooth animations
- Responsive layout
- Beautiful gradients
- Professional styling

## Customization Examples

### Change Logo Text
Edit `templates/base.html`:
```html
<a href="..." class="logo">
    🛍️ Your Store Name  <!-- Change this -->
</a>
```

### Change Primary Color
Edit `static/css/style.css`:
```css
:root {
    --primary-color: #YOUR_COLOR_HERE;
}
```

### Add Your Products
1. Go to `/admin/products/`
2. Click "Add product"
3. Fill in details
4. Upload product image
5. Click Save

### Add Product Categories
1. Go to `/admin/products/category/`
2. Click "Add category"
3. Enter category name
4. Click Save

## Troubleshooting

### Port 8000 Already in Use?
```bash
python manage.py runserver 8001
```

### Database Issues?
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py load_sample_data
```

### CSS/JS Not Loading?
```bash
python manage.py collectstatic --clear --noinput
```

### Missing Dependencies?
```bash
pip install --upgrade -r requirements.txt
```

## Next: Production Deployment

When ready to deploy:

1. Read `SETUP_GUIDE.md` for detailed production setup
2. Review `README.md` for complete documentation
3. Configure environment variables
4. Choose hosting platform
5. Deploy with confidence

---

## Need Help?

- Check `SETUP_GUIDE.md` for detailed setup instructions
- Check `README.md` for complete documentation
- Review Django docs: https://docs.djangoproject.com/
- Check django-allauth docs: https://django-allauth.readthedocs.io/

**Enjoy your modern e-commerce platform! 🚀**
