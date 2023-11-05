from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from products.forms import CustomerUserForm

def register(request):
    form = CustomerUserForm()
    if request.method == "POST":
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully! Login to continue")
            return redirect('/login')
    context = {'form' : form}
    return render(request, "auth/register.html", context)

def loginpage(request):
    return render(request, "auth/login.html")