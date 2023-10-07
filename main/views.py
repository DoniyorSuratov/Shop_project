from django.shortcuts import render

from .models import Product


# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def category(request):
    return render(request, 'category.html')

def product_details(request):
    return render(request, 'single-product.html')

def checkout(request):
    return render(request, 'checkout.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def cart(request):
    return render(request, 'cart.html')

def blog(request):
    return render(request, 'blog.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def login_(request):
    return render(request, 'login.html')

def register_(request):
    return render(request, 'register.html')

def tracking_order(request):
    return render(request, 'tracking-order.html')

def contact(request):
    return render(request, 'contact.html')