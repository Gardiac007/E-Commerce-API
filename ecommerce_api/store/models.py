from django.db import models
from django.contrib.auth.models import AbstractUser     # Import the Django's default User

class User(AbstractUser):   #Inherits django's in-built AbstractUser which contains username, email, etc.

    is_customer = models.BooleanField(default=True)     # Role based logic
    is_seller = models.BooleanField(default=False)

class Category(models.Model):

    category_name = models.CharField(max_length=100) 

    def __str__(self):
        return self.category_name       # Returns the Category name when queried  

class Product(models.Model):

    seller = models.ForeignKey(User, on_delete=models.CASCADE)      # Links the product to the seller
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    # Links the product to the category
    in_stock = models.BooleanField(default=True, null=True)

    def __str__(self): 
        return self.product_name        # Returns the Product name when queried.

class Order(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE)    #Links the Order to the customer
    created_at = models.DateTimeField(auto_now_add=True)        # Create Timestamp when it was created

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)    # Links a specific item to an Order
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)   

