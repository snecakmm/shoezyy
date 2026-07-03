import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart
from .models import Order, OrderItem

@login_required
def checkout(request):
    """Checkout page."""
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        messages.error(request, 'Your cart is empty!')
        return redirect('products:home')
    
    if cart.items.count() == 0:
        messages.error(request, 'Your cart is empty!')
        return redirect('products:home')
    
    if request.method == 'POST':
        # Create order
        order_number = str(uuid.uuid4())[:8].upper()
        
        payment_method = request.POST.get('payment_method', 'cod')
        allowed_payment_methods = {'gpay', 'paytm', 'cod'}
        if payment_method not in allowed_payment_methods:
            payment_method = 'cod'

        order = Order.objects.create(
            user=request.user,
            order_number=order_number,
            shipping_name=request.POST.get('name'),
            shipping_email=request.POST.get('email'),
            shipping_phone=request.POST.get('phone'),
            shipping_address=request.POST.get('address'),
            shipping_city=request.POST.get('city'),
            shipping_state=request.POST.get('state'),
            shipping_postal_code=request.POST.get('postal_code'),
            shipping_country=request.POST.get('country'),
            subtotal=cart.get_total_price(),
            shipping_cost=0,  # Can be calculated based on location
            tax=0,  # Can be calculated based on location
            total=cart.get_total_price(),
            payment_method=payment_method,
        )


        
        # Create order items
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.get_display_price(),
            )
        
        # Clear cart
        cart.items.all().delete()
        
        messages.success(request, 'Order placed successfully!')
        return redirect('orders:order_detail', order_id=order.id)
    
    context = {
        'cart': cart,
        'cart_total': cart.get_total_price(),
    }
    return render(request, 'orders/checkout.html', context)

@login_required
def order_list(request):
    """View user's orders."""
    orders = request.user.orders.all()
    context = {'orders': orders}
    return render(request, 'orders/order_list.html', context)

@login_required
def order_detail(request, order_id):
    """View order details."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'order': order}
    return render(request, 'orders/order_detail.html', context)
