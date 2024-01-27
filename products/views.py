from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


# Create your views here.
def home(request):
    category = Category.objects.filter(status=0)
    context = {'category' : category}
    return render(request,"products/home.html", context)

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category' : category}
    return render(request, "collections.html", context)

def view_collections(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products= Product.objects.filter(Category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {'products' : products, 'category_name' : category_name}
        return render(request, "products/index.html", context)
    else:
        messages.warning(request, "No Category found")
        return redirect('collections')
    
def view_collections_2(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        category_name = Category.objects.filter(slug=slug).first()
        context = {'category_name' : category_name}
        return render(request, "products/index.html", context)
    else:
        messages.warning(request, "No Category found")
        return redirect('collections')
    
def view_products(request, category_slug, product_slug):
    if (Category.objects.filter(slug=category_slug, status=0)):
        if (Product.objects.filter(slug=product_slug, status=0)):
            products = Product.objects.filter(slug=product_slug, status=0).first()
            context = {"products" : products}

        else:
            messages.error(request, "No product found")
            return redirect('collections')
    else:
        messages.error(request, "No category found")
        return redirect('collections')
    
    return render(request, "products/view.html", context)

def view_all_products(request):
    if (Product.objects.filter(status=0)):
        products = Product.objects.filter(status=0)
        context = {"products" : products}
    else:
        messages.error(request, "No product found")
        return redirect('home')
    
    return render(request, "products/view-all-products.html", context)

def view_all_category(request):
    if (Product.objects.filter(status=0)):
        category = Category.objects.filter(status=0)
        context = {"category" : category}
    else:
        messages.error(request, "No category found")
        return redirect('home')
    
    return render(request, "products/view-all-products.html", context)


def java_script(request):
    filename = request.path.strip("/")
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/javascript")