"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static

from products.controller import authview, cart, wishlist, checkout, order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/',views.home, name='home'),
    
    path('collections/', views.collections, name="collections"),
    path('collections/<str:slug>', views.view_collections, name="view_collections"),
    path('collections/<str:category_slug>/<str:product_slug>', views.view_products, name='view_products'),
    path('all-products/', views.view_all_products, name="viewallproducts"),
    
    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),
    
    path('add-to-cart/', cart.addtocart, name="addtocart" ),
    path('cart/', cart.viewcart, name="cart"),
    path('update-cart/', cart.updatecart, name = "updatecart"),
    path('remove-cart-item/', cart.removecartitem, name="removecartitem"),
    
    path('wishlist/', wishlist.index, name="wishlist"),
    path('add-to-wishlist/', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item/', wishlist.deletewishlistitem, name="deletewishlistitem"),
    
    path('checkout/', checkout.index, name="checkout"),
    path('place-order',checkout.placeorder, name='placeorder'),
    
    path('my-orders/', order.index, name="myorders"),
    path('view-order/<str:t_no>', order.vieworder, name="orderview"),
]   


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)