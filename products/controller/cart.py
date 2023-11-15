from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from products.forms import CustomerUserForm
from products.models import Product, Cart
from django.contrib.auth.decorators import login_required


def addtocart(request):
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
                        return JsonResponse({'status' : "Only " + str(product_check.quantity) + " Stocks available for this product."})
            else:
                return JsonResponse({'status' : "No such product found"})
        else:
            return JsonResponse({'status' : "Login to Continue"})
    return redirect('collections')



@login_required(login_url='loginpage')
def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart' : cart}
    return render(request, "cart.html", context)


def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            product_item = Product.objects.get(id=prod_id)
            cart.product_qty = prod_qty
            if product_item.quantity < cart.product_qty:
                return JsonResponse({"status" : "Product Quantity exceeds available stock"})
            else:
                cart.save()
            return JsonResponse({"status" : "Product Quantity Updated Successfully"})
    return redirect('collections')           

def removecartitem(request):
    if request.method == "POST" :
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            cart_item = Cart.objects.get(product_id=prod_id, user=request.user)
            cart_item.delete()
        return JsonResponse({'status' : "Product Removed Successfully"})
    return redirect('collections')