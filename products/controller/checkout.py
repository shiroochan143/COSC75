from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product, Cart

def index(request):
    raw_cart = Cart.objects.filter(user=request.user)
    for item in raw_cart:
        if item.product_qty > item.product.quantity:
            remove_item = Cart.objects.get(id=item.id)
            remove_item.delete()
            #Cart.objects.delete(id=item.id)    
    
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart_items:
        total_price = total_price + item.product.selling_price * item.product_qty
        
    context = {'cart_items' : cart_items, 'total_price' : total_price}
    return render(request, "checkout.html", context)