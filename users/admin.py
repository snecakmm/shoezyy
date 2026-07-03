from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'avatar', 'bio', 'date_of_birth', 'address', 'city', 'state', 'postal_code', 'country', 'is_verified')}),
    )
    list_display = ['email', 'first_name', 'last_name', 'phone', 'is_verified', 'created_at']
    search_fields = ['email', 'first_name', 'last_name', 'phone']
