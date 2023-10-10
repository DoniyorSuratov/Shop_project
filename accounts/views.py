from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, hashers
User = get_user_model()

def register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        print("username:", username)

        if password == confirmPassword:
            if User.objects.filter(email=email).exists():
                print("Email already exists!")
                return redirect('/accounts/register')
            if User.objects.filter(username=username).exists():
                print("Username already exists!")
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
            print("Passwords are not common! ")
            return redirect('accounts/register')
    return render(request, 'register.html')



def login(request):
    return render(request, 'login.html')