import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

try:
    user = User.objects.get(username='sabith')
    user.set_password('sabith364')
    user.save()
    print(f'✓ Password set for user: sabith')
    print(f'✓ Admin credentials: username=sabith, password=sabith364')
except User.DoesNotExist:
    print('User "sabith" not found')
