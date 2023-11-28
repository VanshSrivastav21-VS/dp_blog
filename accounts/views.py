from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    #agar from submit hoto
    if request.method =="POST":
        # form se data alag alag variable me store karo
        username = request.Post.get('username')
        email = request.Post.get('email')
        password = request.Post.get('password')
        cpassword = request.Post.get('cpassword')
        if password != cpassword and len(password) == 0 or len(cpassword) == 0:
            messages.error(request, "Password do not match")
            return redirect('register')
        #user create karo
        user = User.objects.create_user(username, email, password)
        messages.success(request, "Account created successfully")
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')
    
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email) == 0 or len(password) == 0:
           messages.error(request, "Invalid credebtialist")
           return redirect('login')
        #user authentication karo
        user = authenticate(request, email=email, password=password)
        if user is not None:
            messages.success(request, "Logged in successfully")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid creadebtals!")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
    
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')

def profile_view(request):
    return render(request, 'accounts/profile.html')


