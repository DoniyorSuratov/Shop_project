from django.urls import path
from  .views import (home,
                     category,
                     product_details,
                     checkout,
                     confirmation,
                     cart,
                     blog,
                     single_blog,
                     tracking_order,
                     contact)

urlpatterns=[
    path('', home, name='home'),
    path('category', category, name='category'),
    path('single-product', product_details, name='product_details'),
    path('checkout', checkout, name='checkout'),
    path('confirmation',confirmation, name='confirmation' ),
    path('cart',cart, name='chart'),
    path('blog', blog, name='blog'),
    path('single-blog', single_blog, name='single_blog'),
    path('tracking-order', tracking_order, name='tracking_order'),
    path('contact', contact, name='contact')

]