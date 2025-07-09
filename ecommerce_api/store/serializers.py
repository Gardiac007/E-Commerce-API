from rest_framework import serializers
from .models import Category, Product, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):      # ModelSerializer - automatically maps models fields to serializer fields

    class Meta:     # It tells the ModelSerializer how to behave 

        model = Category
        fields = '__all__'       # include all the fields from the Category model

class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only = True)     # Nested Serializer = It will embed category details to product

    class Meta:

        model = Product
        fields = '__all__'
        read_only_fields = ['seller']

class OrderItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source = 'product.product_name', read_only = True)     #It will add product_name field takes from the Product Model

    class Meta:

        model = OrderItem
        fields = ['id', 'order', 'product', 'product_name', 'quantity']     # Manually declare fields to be serialized instead of include all fields

class OrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = '__all__'
        read_only_fields = ['product_name']