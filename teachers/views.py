# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def register_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Teacher registered successfully.")
            return redirect('login_teacher')
    return render(request, 'register.html')

def login_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'login.html')

def logout_teacher(request):
    logout(request)
    return redirect('login_teacher')
