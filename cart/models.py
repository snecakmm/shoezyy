from django.db import models
from django.contrib.sessions.models import Session
from products.models import Product
from users.models import CustomUser

class Cart(models.Model):
    """Shopping cart model."""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.email if self.user else self.session_key}"

    def get_total_price(self):
        """Calculate total price of all items in cart."""
        return sum(item.get_total_price() for item in self.items.all())

    def get_total_items(self):
        """Get total number of items in cart."""
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    """Items in shopping cart."""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['cart', 'product']

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_total_price(self):
        """Get total price for this item."""
        return self.product.get_display_price() * self.quantity
