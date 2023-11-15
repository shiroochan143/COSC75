from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from products.forms import CustomerUserForm

def register(request):
    form = CustomerUserForm()
    if request.method == "POST":
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully! Login to continue")
            return redirect('loginpage')
    context = {'form' : form}
    return render(request, "auth/register.html", context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect('loginpage')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username = name, password = passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful, Welcome!")
                return redirect('collections')
            else:
                messages.error(request, "Invalid Username or Password. Please try again!")
                return redirect('loginpage')
    return render(request, "auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged Out Successfully!")
    return redirect('loginpage')