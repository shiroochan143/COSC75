from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from products.models import Product, Cart, Order, OrderItem, Profile
import random

@login_required(login_url='loginpage')
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
        
    user_profile = Profile.objects.filter(user=request.user).first()
        
    context = {'cart_items' : cart_items, 'total_price' : total_price, 'user_profile' : user_profile}
    return render(request, "checkout.html", context)

@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == "POST":
        
        current_user = User.objects.filter(id=request.user.id).first()
        
        if not current_user.first_name :
            current_user.first_name = request.POST.get('fname')
            current_user.last_name = request.POST.get('lname')
            current_user.save()
            
        if not Profile.objects.filter(user=request.user):
            user_profile = Profile()
            user_profile.user = request.user
            user_profile.phonenumber = request.POST.get("phonenumber")
            user_profile.address= request.POST.get("address")
            user_profile.province = request.POST.get("province")
            user_profile.city = request.POST.get("city")
            user_profile.zipcode = request.POST.get("zipcode")
            user_profile.save()
            
            
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get("fname")
        neworder.lname = request.POST.get("lname")
        neworder.email = request.POST.get("email")
        neworder.phonenumber = request.POST.get("phonenumber")
        neworder.address= request.POST.get("address")
        neworder.province = request.POST.get("province")
        neworder.city = request.POST.get("city")
        neworder.zipcode = request.POST.get("zipcode")
        
        neworder.payment_mode = request.POST.get("payment_mode")
        
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0 
        for item in cart:
            cart_total_price = cart_total_price + (item.product.selling_price * item.product_qty)
            
        neworder.total_price = cart_total_price
        track_number = 'kmart'+str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_number = track_number) is None:
            track_number = 'kmart'+str(random.randint(1111111, 9999999))
            
        neworder.tracking_number =track_number
        neworder.save()
        
        neworder_items = Cart.objects.filter(user=request.user)
        for item in neworder_items:
            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.selling_price,
                quantity= item.product_qty,
            )
            
        #decrease the product quantity from available stock
        order_product = Product.objects.filter(id=item.product_id).first()
        order_product.quantity = order_product.quantity - item.product_qty
        order_product.save()
        
        #clear the user's cart
        Cart.objects.filter(user = request.user).delete()
        
        messages.success(request, "Your order has been placed successfully")
        
    return redirect('collections')