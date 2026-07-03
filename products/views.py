from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category, Review

def home(request):
    """Home page with featured products."""
    featured_products = Product.objects.filter(featured=True)[:8]
    categories = Category.objects.all()[:6]
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'products/home.html', context)

def product_list(request):
    """Product listing page with filters."""
    products = Product.objects.all()
    categories = Category.objects.all()
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Sort
    sort = request.GET.get('sort', '-created_at')
    if sort in ['price', '-price', 'name', '-created_at', 'rating']:
        products = products.order_by(sort)
    
    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_slug,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, slug):
    """Product detail page."""
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    reviews = product.product_reviews.all().order_by('-created_at')
    
    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
    }
    return render(request, 'products/product_detail.html', context)

def category_detail(request, slug):
    """Category detail page."""
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products/category_detail.html', context)
