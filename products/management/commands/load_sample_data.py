from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Load sample data for the store'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Latest electronics and gadgets'},
            {'name': 'Fashion', 'description': 'Trendy fashion items'},
            {'name': 'Home & Garden', 'description': 'Home and garden products'},
            {'name': 'Sports', 'description': 'Sports and fitness gear'},
        ]

        categories = {}
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = cat
            if created:
                self.stdout.write(f"Created category: {cat.name}")

        # Create products
        products_data = [
            {
                'name': 'Wireless Headphones',
                'category': 'Electronics',
                'description': 'Premium wireless headphones with noise cancellation',
                'price': Decimal('199.99'),
                'discount_price': Decimal('149.99'),
                'stock': 50,
                'featured': True,
            },
            {
                'name': 'Smart Watch',
                'category': 'Electronics',
                'description': 'Advanced fitness tracking smartwatch',
                'price': Decimal('299.99'),
                'discount_price': Decimal('249.99'),
                'stock': 30,
                'featured': True,
            },
            {
                'name': 'Laptop Stand',
                'category': 'Electronics',
                'description': 'Adjustable aluminum laptop stand',
                'price': Decimal('79.99'),
                'stock': 100,
                'featured': False,
            },
            {
                'name': 'Designer Sunglasses',
                'category': 'Fashion',
                'description': 'UV protection designer sunglasses',
                'price': Decimal('159.99'),
                'discount_price': Decimal('119.99'),
                'stock': 40,
                'featured': True,
            },
            {
                'name': 'Premium Backpack',
                'category': 'Fashion',
                'description': 'Durable and stylish travel backpack',
                'price': Decimal('129.99'),
                'stock': 60,
                'featured': False,
            },
            {
                'name': 'Yoga Mat',
                'category': 'Sports',
                'description': 'Non-slip yoga and exercise mat',
                'price': Decimal('49.99'),
                'stock': 80,
                'featured': True,
            },
            {
                'name': 'Dumbbell Set',
                'category': 'Sports',
                'description': 'Complete home gym dumbbell set',
                'price': Decimal('249.99'),
                'discount_price': Decimal('199.99'),
                'stock': 25,
                'featured': True,
            },
            {
                'name': 'LED Desk Lamp',
                'category': 'Home & Garden',
                'description': 'Modern LED desk lamp with USB charging',
                'price': Decimal('89.99'),
                'stock': 45,
                'featured': False,
            },
        ]

        for prod_data in products_data:
            category = categories[prod_data.pop('category')]
            prod, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={**prod_data, 'category': category}
            )
            if created:
                self.stdout.write(f"Created product: {prod.name}")

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data!'))
