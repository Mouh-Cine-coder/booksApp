from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.




def register(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('signup_username', '').strip()
        print(username)
        email = request.POST.get('signup_email', '').strip()
        
        first_name = request.POST.get('signup_first_name', ).strip()
        last_name = request.POST.get('signup_last_name', '').strip()
        
        if 'signup_password' in request.POST and 'signup_password_confirmation' in request.POST:
            password = request.POST['signup_password']
            password_confirmation = request.POST['signup_password_confirmation']
        else:
           
            messages.warning(request, "password or password confirmation are missing")
            return render(request, './auth/registration.html')

        if not password == password_confirmation:
            
            messages.warning(request, "password doesn't match")
            return render(request, './auth/registration.html')

        
        if not Customer.objects.filter(username=username).exists():
            user = Customer.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password_confirmation),
                is_staff=False,
                is_superuser=False
            )
            user.save()
            messages.success(request, "user created successefuly")
            return redirect('signin')
        else:
           
            messages.warning(request, "user already exists")
            return render(request, './auth/registration.html')

    return render(request, './auth/registration.html')


def signin(request):
      
    if request.method == 'POST':
        username = request.POST.get('login_username', '').strip()
        
        if 'login_password' in request.POST:
            password = request.POST['login_password']
        else:
            messages.warning(request, "password missing")
            return render(request, './auth/login.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "login successefuly")
            return redirect("/")
        else:
            messages.warning(request, "Wrong credentails")
            return render(request, './auth/login.html')
            
    return render(request, './auth/login.html')

