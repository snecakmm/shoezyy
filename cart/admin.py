from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'session_key', 'get_total_items', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['user__email', 'session_key']
    inlines = [CartItemInline]
    readonly_fields = ['created_at', 'updated_at']

    def get_total_items(self, obj):
        return obj.get_total_items()
    get_total_items.short_description = 'Total Items'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', 'updated_at']
    list_filter = ['updated_at']
    search_fields = ['product__name', 'cart__user__email']
