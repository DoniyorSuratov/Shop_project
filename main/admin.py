from django.contrib import admin
from .models import Product, Images, Categories
# Register your models here.

admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Images)
