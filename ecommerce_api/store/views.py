from rest_framework import viewsets, filters
from .models import Category, Product, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, OrderItemSerializer
from .permissions import IsSellerOrReadOnly, IsCustomerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
    
class ProductView(viewsets.ModelViewSet):       # ModelViewset provide CRUD API operations

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSellerOrReadOnly]      # check the user is Seller and is authenticated
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]       # Filter by Search and Sorting by Ordering
    filterset_fields = ['category', 'in_stock']
    search_fields = ['category__category_name', 'product_name']
    ordering_fields = ['price']

class CategoryView(viewsets.ModelViewSet):

    permission_classes = [IsSellerOrReadOnly]      # check the user is Seller and is authenticated
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderView(viewsets.ModelViewSet):

    permission_classes = [IsCustomerOrReadOnly]     # check the user is Customer and is authenticated.
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(customer = self.request.user.id)   # Each user can see their orders only
    
    def perform_create(self, serializer):
        return serializer.save(customer = self.request.user)    # Automatically sets the customer field for an order to the currently logged-in user

class OrderItemToCartView(viewsets.ModelViewSet):

    permission_classes = [IsCustomerOrReadOnly]     # check the user is Customer and is authenticated.

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
