from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal
import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Load shoe products for Sheos collection'

    def handle(self, *args, **options):
        # Create or get Sheos category
        category, created = Category.objects.get_or_create(
            name='Sheos',
            defaults={'description': 'Premium footwear collection'}
        )
        if created:
            self.stdout.write(f"Created category: {category.name}")

        shoes_data = [
            {
                'name': 'Urban Street Sneakers',
                'description': 'Comfortable and stylish sneakers perfect for everyday wear. Features premium cushioning and breathable mesh material.',
                'price': Decimal('89.99'),
                'discount_price': Decimal('69.99'),
                'stock': 45,
                'featured': True,
            },
            {
                'name': 'Classic Canvas Slip-On',
                'description': 'Timeless canvas shoes with rubber sole. Perfect for casual outings and weekend adventures.',
                'price': Decimal('59.99'),
                'discount_price': Decimal('44.99'),
                'stock': 60,
                'featured': True,
            },
            {
                'name': 'Running Performance Shoe',
                'description': 'Designed for runners. Advanced cushioning technology and lightweight design for optimal performance.',
                'price': Decimal('129.99'),
                'discount_price': Decimal('99.99'),
                'stock': 35,
                'featured': True,
            },
            {
                'name': 'Elegant Formal Loafers',
                'description': 'Premium leather loafers ideal for formal occasions. Handcrafted with attention to detail.',
                'price': Decimal('149.99'),
                'discount_price': Decimal('119.99'),
                'stock': 28,
                'featured': True,
            },
            {
                'name': 'Adventure Trail Boots',
                'description': 'Rugged outdoor boots with waterproof protection. Perfect for hiking and outdoor exploration.',
                'price': Decimal('179.99'),
                'discount_price': Decimal('139.99'),
                'stock': 32,
                'featured': True,
            },
            {
                'name': 'Summer Beach Sandals',
                'description': 'Comfortable and lightweight sandals for summer. Easy to slip on and perfect for beach days.',
                'price': Decimal('39.99'),
                'stock': 85,
                'featured': True,
            },
            {
                'name': 'Premium Basketball High-Top',
                'description': 'High-performance basketball shoes with ankle support and cushioned sole for court domination.',
                'price': Decimal('159.99'),
                'discount_price': Decimal('119.99'),
                'stock': 25,
                'featured': True,
            },
            {
                'name': 'Minimalist Leather Oxfords',
                'description': 'Sleek and sophisticated oxford shoes. Perfect for professional settings and formal events.',
                'price': Decimal('189.99'),
                'discount_price': Decimal('149.99'),
                'stock': 18,
                'featured': True,
            },
        ]

        for shoe_data in shoes_data:
            # Check if product already exists
            product, created = Product.objects.get_or_create(
                name=shoe_data['name'],
                category=category,
                defaults={
                    'description': shoe_data['description'],
                    'price': shoe_data['price'],
                    'discount_price': shoe_data.get('discount_price'),
                    'stock': shoe_data['stock'],
                    'featured': shoe_data.get('featured', False),
                }
            )
            
            # Generate a placeholder image if product doesn't have one
            if created and not product.image:
                # Create a simple colored image as placeholder
                img = Image.new('RGB', (300, 300), color=self._get_color(shoe_data['name']))
                img_io = BytesIO()
                img.save(img_io, 'JPEG', quality=85)
                img_io.seek(0)
                
                # Save the image to the product
                product.image.save(
                    f"{product.slug}.jpg",
                    ContentFile(img_io.getvalue()),
                    save=False
                )
                product.save()
                self.stdout.write(f"Created product: {product.name} with placeholder image")
            else:
                self.stdout.write(f"Product already exists: {product.name}")

        self.stdout.write(self.style.SUCCESS("Successfully loaded shoe products"))

    def _get_color(self, name):
        """Generate a consistent color based on product name"""
        colors = [
            (99, 102, 241),      # Primary - indigo
            (236, 72, 153),      # Secondary - pink
            (16, 185, 129),      # Success - green
            (249, 115, 22),      # Warning - orange
            (168, 85, 247),      # Purple
            (59, 130, 246),      # Blue
            (239, 68, 68),       # Red
            (34, 197, 94),       # Green
        ]
        hash_val = sum(ord(c) for c in name)
        return colors[hash_val % len(colors)]
