from rest_framework.permissions import BasePermission, SAFE_METHODS     # BasePermission used for Custom permissions

class IsSellerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_seller     #Returns True when User is both authenticated and Seller


class IsCustomerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_customer   #Returns True when User is both authenticated and Customer