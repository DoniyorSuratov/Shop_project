from django.shortcuts import render

from .models import Product, Images


# Create your views here.

def home(request):
    products = Product.objects.all()[0:4]
    products_data = []
    for product in products:
        image = Images.objects.filter(product=product).first()  # select * from image where product id = product_id
        product.image = image
        products_data.append(image)

    products2 = Product.objects.all()[4:9]
    products_data2 = []
    for product in products2:
        image = Images.objects.filter(product=product).first()  # select * from image where product id = product_id
        product.image = image
        products_data2.append(image)

    products_data3 = []
    products3 = Product.objects.all()[9:12]
    for product in products3:
        image = Images.objects.filter(product=product).first()  # select * from image where product id = product_id
        product.image = image
        products_data3.append(image)
    return render(request, 'index.html', {'products': products,
                                          'products2': products2,
                                          'products3': products3})


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
