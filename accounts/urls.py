from django.urls import path

from .views import register, sign_in

urlpatterns = [
    path('register', register),
    path('login', sign_in)
]