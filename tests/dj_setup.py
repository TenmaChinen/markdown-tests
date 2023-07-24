import django, os, sys

sys.path.append('..') # THIS NEEDED TO ACCESS TOP PARENT
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()