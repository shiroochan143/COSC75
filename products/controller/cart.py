from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from products.forms import CustomerUserForm
from products.models import Product, Cart

def addtocart(request):
    print("add to cart view called")
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            prod_qty = int(request.POST.get("product_qty"))
            product_check = Product.objects.get(id = prod_id)
            if (product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status' : "Product already in cart!"})
                else:
    
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status' : "Product added successfully"})
                    else:
                        return JsonResponse({'status' : "Only" + str(product_check.quantity)} + " quantity available.")
            else:
                return JsonResponse({'status' : "No such product found"})
        else:
            return JsonResponse({'status' : "Login to Continue"})
    return redirect('collections')


def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart' : cart}
    return render(request, "products/cart.html", context)