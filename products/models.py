from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.utils import timezone
import datetime
from datetime import timedelta
import os

# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    now_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (now_time, original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_timestamp(self):
        # Convert the timestamp to the local timezone
        local_offset = timedelta(hours=8)  # Replace with your actual offset

        # Apply the offset to the timestamp
        local_time = self.created_at + local_offset
        # Format the timestamp as a string
        return local_time.strftime('%Y-%m-%d %I:%M:%S %p')

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    product_description = models.TextField(max_length=500, null=False, blank=False)
    
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False) 
    selling_price = models.FloatField(null=False, blank=False)
    
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=150, null=False, blank=False)

    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_timestamp(self):
        # Convert the timestamp to the local timezone
        local_offset = timedelta(hours=8)  # Replace with your actual offset

        # Apply the offset to the timestamp
        local_time = self.created_at + local_offset
        # Format the timestamp as a string
        return local_time.strftime('%Y-%m-%d %I:%M:%S %p')
    
    def __str__(self):
        return self.name
    
   

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def formatted_timestamp(self):
        # Convert the timestamp to the local timezone
        local_offset = timedelta(hours=8)  # Replace with your actual offset

        # Apply the offset to the timestamp
        local_time = self.created_at + local_offset
        # Format the timestamp as a string
        return local_time.strftime('%Y-%m-%d %I:%M:%S %p')
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def formatted_timestamp(self):
        # Convert the timestamp to the local timezone
        local_offset = timedelta(hours=8)  # Replace with your actual offset

        # Apply the offset to the timestamp
        local_time = self.created_at + local_offset
        # Format the timestamp as a string
        return local_time.strftime('%Y-%m-%d %I:%M:%S %p')
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phonenumber = models.CharField(max_length=150, null=False)
    address = models.TextField(max_length=350, null=False)
    city = models.CharField(max_length=150, null=False)
    province = models.CharField(max_length=150, null=False)
    zipcode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=150, null=True)
    order_status = ('Order Pending', 'Order Pending'), ('Out for Shipping', 'Out for Shipping'), ('Order Complete', 'Order Complete')
    status = models.CharField(max_length=150, choices=order_status, default="Pending")
    message = models.TextField(null=True)
    tracking_number = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def formatted_timestamp(self):
        # Convert the timestamp to the local timezone
        local_offset = timedelta(hours=8)  # Replace with your actual offset

        # Apply the offset to the timestamp
        local_time = self.created_at + local_offset
        # Format the timestamp as a string
        return local_time.strftime('%Y-%m-%d %I:%M:%S %p')
    
    def __str__(self):
        return f"{self.id} - {self.tracking_number}"
    
    def formatted_timestamp2(self):
        # Convert the timestamp to the local timezone
        local_offset = timedelta(hours=8)  # Replace with your actual offset

        # Apply the offset to the timestamp
        local_time = self.updated_at + local_offset
        # Format the timestamp as a string
        return local_time.strftime('%Y-%m-%d %I:%M:%S %p')
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    
    def __str__(self):
        return f"{self.order.id} - {self.order.tracking_number}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=50, null=False)
    province = models.CharField(max_length=50, null=False)
    zipcode = models.CharField(max_length=50, null=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def formatted_timestamp(self):
        # Convert the timestamp to the local timezone
        local_offset = timedelta(hours=8)  # Replace with your actual offset

        # Apply the offset to the timestamp
        local_time = self.created_at + local_offset
        # Format the timestamp as a string
        return local_time.strftime('%Y-%m-%d %I:%M:%S %p')
    
    def __str__(self):
        return self.user.username
    
    