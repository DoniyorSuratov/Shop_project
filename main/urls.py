from django.urls import path
from  .views import (home,
                     category,
                     product_details,
                     checkout,
                     confirmation,
                     cart,
                     blog,
                     single_blog,
                     login_,
                     register_,
                     tracking_order,
                     contact)

urlpatterns=[
    path('', home),
    path('category', category),
    path('single-product', product_details),
    path('checkout', checkout),
    path('confirmation',confirmation ),
    path('cart',cart),
    path('blog', blog),
    path('single-blog', single_blog),
    path('login', login_),
    path('register', register_),
    path('tracking-order', tracking_order),
    path('contact', contact)

]