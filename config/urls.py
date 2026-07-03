"""
URL configuration for sheozy project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/users/', include('users.urls')),
    path('api/products/', include(('products.urls', 'products'), namespace='products_api')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('', include('products.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
