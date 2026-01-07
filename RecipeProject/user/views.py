from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_page(request):

    if request.method =="POST":
        user_name = request.POST.get("user_name")
        user_email = request.POST.get("user_email")
        user_first_name = request.POST.get("user_first_name")
        user_last_name = request.POST.get("user_last_name")
        user_password = request.POST.get("user_password")
        user_repassword = request.POST.get("user_repassword")

        if User.objects.filter(username = user_name).exists():
            messages.error(request, "Username already taken!")
            return redirect("/user/register")
        
        if User.objects.filter(email = user_email).exists():
            messages.error(request, "Email already registered!")
            return redirect("/user/register")

        if user_password != user_repassword:
            messages.error(request, "Passwords donot match")
            return redirect("/user/register")

        user = User.objects.create_user(user_name, user_email, user_password)
        user.first_name = user_first_name
        user.last_name = user_last_name
        user.save()
        messages.success(request, "User registered successfully!")
        return redirect("/user/login")

    return render(request, 'user/register.html')

def login_page(request):

    if request.method == "POST":
        user_name_email = request.POST.get("user_name_email")
        user_password = request.POST.get("user_password")

        try:
            user = User.objects.get(username = user_name_email)
            
        except User.DoesNotExist:
            try:
                user = User.objects.get(email = user_name_email)
            except User.DoesNotExist:
                messages.error(request, "Email or username doesnot exist!")
                return redirect('/user/login')
    
        user = authenticate(username = user.username, password = user_password)

        if user is None:
            messages.error(request, "Incorrect password!")
            return redirect("/user/login")
        
        login(request, user)
        return redirect("/")

    return render(request, 'user/login.html')

def logout_page(request):

    logout(request)
    return redirect("/")
