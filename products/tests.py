from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Product, Cart, Wishlist, Order, OrderItem

class AccountsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login(self):
        # Test login functionality
        response = self.client.post(reverse('loginpage'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        # Test logout functionality
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_registration(self):
        # Test user registration
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser+test@gmail.com',
            'password1': 'newpassword',
            'password2': 'newpassword',
        })
        self.assertEqual(response.status_code, 200)

class ModelsTestCase(TestCase):
    def setUp(self):
        # Create a test user for related models
        self.test_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_category_model(self):
        category = Category.objects.create(
            slug='test-category',
            name='Test Category',
            description='Test category description',
            meta_title='Test Category',
            meta_keywords='test, category',
            meta_description='Test category meta description',
        )
        self.assertEqual(str(category), 'Test Category')

    def test_product_model(self):
        category = Category.objects.create(
            slug='test-category',
            name='Test Category',
            description='Test category description',
            meta_title='Test Category',
            meta_keywords='test, category',
            meta_description='Test category meta description',
        )
        product = Product.objects.create(
            Category=category,
            slug='test-product',
            name='Test Product',
            product_description='Test product description',
            quantity=50,
            original_price=50.0,
            selling_price=40.0,
            tag='Test Tag',
            meta_title='Test Product',
            meta_keywords='test, product',
            meta_description='Test product meta description',
        )
        self.assertEqual(str(product), 'Test Product')

    def test_cart_model(self):
        cart = Cart.objects.create(
            user=self.test_user,
            product=Product.objects.create(Category=Category.objects.create(), slug='test-product', name='Test Product'),
            product_qty=2,
        )
        self.assertEqual(str(cart), 'Cart item for user: testuser, product: Test Product')

    def test_wishlist_model(self):
        wishlist = Wishlist.objects.create(
            user=self.test_user,
            product=Product.objects.create(Category=Category.objects.create(), slug='test-product', name='Test Product'),
        )
        self.assertEqual(str(wishlist), 'Wishlist item for user: testuser, product: Test Product')

    def test_order_model(self):
        order = Order.objects.create(
            user=self.test_user,
            fname='John',
            lname='Doe',
            email='john@example.com',
            phonenumber='1234567890',
            address='Test Address',
            city='Test City',
            province='Test Province',
            zipcode='12345',
            total_price=100.0,
            payment_mode='Card',
            tracking_number='123ABC',
        )
        self.assertEqual(str(order), '1 - 123ABC')

    def test_order_item_model(self):
        order = Order.objects.create(
            user=self.test_user,
            fname='John',
            lname='Doe',
            email='john@example.com',
            phonenumber='1234567890',
            address='Test Address',
            city='Test City',
            province='Test Province',
            zipcode='12345',
            total_price=100.0,
            payment_mode='Card',
            tracking_number='123ABC',
        )
        product = Product.objects.create(Category=Category.objects.create(), slug='test-product', name='Test Product')
        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            price=50.0,
            quantity=2,
        )
        self.assertEqual(str(order_item), '1 - 123ABC')