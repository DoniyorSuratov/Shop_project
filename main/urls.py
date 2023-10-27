from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from  .views import (HomeView,
                     CategoryView,
                     ProductDetailView,
                     ShoppingCartView,
                     CheckoutView,
                     confirmation,
                     BlogView,
                     single_blog,
                     ShoppingHistoryView,
                     IncrementCountAPIView,
                     DecrementCountAPIView,
                     ChangeCountAPIView,
                     AddPhotosView
                     )

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('category', CategoryView.as_view(), name='category'),
    path('single-product', ProductDetailView.as_view(), name='product_details'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('confirmation',confirmation, name='confirmation' ),
    path('cart',ShoppingCartView.as_view(), name='chart'),
    path('blog', BlogView.as_view(), name='blog'),
    path('single-blog', single_blog, name='single_blog'),
    path('shopping-history', ShoppingHistoryView.as_view(), name='shopping-history'),
    path('add-photos', AddPhotosView.as_view(), name='add-photos'),





    #API
    path('increment', csrf_exempt(IncrementCountAPIView.as_view()), name='increment'),
    path('decrement', csrf_exempt(DecrementCountAPIView.as_view()), name='decrement'),
    path('change', csrf_exempt(ChangeCountAPIView.as_view()), name='change'),

]