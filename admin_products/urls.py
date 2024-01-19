from django.urls import path
from .views import (
    AdminProductsListCreateAPIView,
    AdminProductRetrieveAPIView,
    AdminProductsRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('admin-products/', AdminProductsListCreateAPIView.as_view(), name='admin-products-list-create'),  # Endpoint for listing and creating admin products
    path('admin-products/<int:pk>/', AdminProductRetrieveAPIView.as_view(), name='admin-product-retrieve'),  # Endpoint for retrieving a specific admin product
    path('admin-products/<int:pk>/update/', AdminProductsRetrieveUpdateDestroyAPIView.as_view(), name='admin-products-retrieve-update-destroy'),  # Endpoint for retrieving, updating, and deleting a specific admin product
]
