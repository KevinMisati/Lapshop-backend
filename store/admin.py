from django.contrib import admin
from .models import Laptop,Brand, Category

# Register your models here.
admin.site.register(Laptop)
admin.site.register(Brand)
admin.site.register(Category)
