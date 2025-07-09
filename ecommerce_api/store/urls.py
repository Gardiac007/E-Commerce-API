from django.urls import path, include
from .views import ProductView, CategoryView, OrderView, OrderItemToCartView
from rest_framework.routers import DefaultRouter        # Automatically generates URL patterns for each endpoints

router = DefaultRouter()
router.register(r'product', ProductView)    # To view the products
router.register(r'category', CategoryView)  # To view the categories
router.register(r'orders', OrderView)   # To view the orders made by the user
router.register(r'orderitem', OrderItemToCartView)

urlpatterns = [
    
    path('', include(router.urls)),

]

