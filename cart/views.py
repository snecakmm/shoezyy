from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from products.models import Product
from .models import Cart, CartItem

def get_or_create_cart(request):
    """Get or create cart for user or session."""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key or request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def cart_view(request):
    """Display shopping cart."""
    cart = get_or_create_cart(request)
    context = {
        'cart': cart,
        'items': cart.items.all(),
    }
    return render(request, 'cart/cart.html', context)

def add_to_cart(request, product_id):
    """Add product to cart."""
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)
    
    quantity = int(request.POST.get('quantity', 1))
    
    # Check stock
    if product.stock < quantity:
        messages.error(request, 'Not enough stock available!')
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': 'Not enough stock'})
        return redirect('products:product_detail', slug=product.slug)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        # Check if new quantity exceeds stock
        new_quantity = cart_item.quantity + quantity
        if product.stock < new_quantity:
            messages.error(request, f'Can only add {product.stock - cart_item.quantity} more items!')
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': 'Not enough stock'})
        else:
            cart_item.quantity += quantity
            cart_item.save()
            messages.success(request, f'{product.name} added to cart!')
    else:
        messages.success(request, f'{product.name} added to cart!')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'total_items': cart.get_total_items(),
            'total_price': float(cart.get_total_price()),
            'redirect_url': request.build_absolute_uri('/cart/')
        })

    return redirect('cart:cart')

def update_cart(request, item_id):
    """Update cart item quantity."""
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    if request.user.is_authenticated:
        if cart_item.cart.user != request.user:
            return redirect('cart:cart')
    
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0:
        cart_item.delete()
        messages.success(request, 'Item removed from cart!')
    else:
        if cart_item.product.stock < quantity:
            messages.error(request, f'Only {cart_item.product.stock} items in stock!')
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated!')
    
    return redirect('cart:cart')

def remove_from_cart(request, item_id):
    """Remove item from cart."""
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    if request.user.is_authenticated:
        if cart_item.cart.user != request.user:
            return redirect('cart:cart')
    
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'{product_name} removed from cart!')
    
    return redirect('cart:cart')

def clear_cart(request):
    """Clear all items from cart."""
    cart = get_or_create_cart(request)
    cart.items.all().delete()
    messages.success(request, 'Cart cleared!')
    return redirect('cart:cart')
