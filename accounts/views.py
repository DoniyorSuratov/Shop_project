from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, hashers, authenticate, login, logout
from django.views import View
from django.contrib import messages
User = get_user_model()

class RegisterView(View):
    template_name = 'register.html'
    context = {}
    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password == confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists!")
                return redirect('/accounts/register')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
                return redirect('/accounts/register')
            else:
                user = User.objects.create(
                    username=username,
                    email=email,
                    password=hashers.make_password(password)
                )
                user.save()
                return redirect('/accounts/login')
        else:
            messages.error(request, "Passwords are not common! ")
            return redirect('/accounts/register')

class LoginView(View):
    template_name = 'login.html'
    context = {}
    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or pasword')
            return redirect('/accounts/login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/accounts/login')



