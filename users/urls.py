from django.urls import path
from .views import all_products, woman_products, kids_products, wedding_products
from .views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    UserRetrieveAPIView,
)

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),  # Endpoint for listing and creating users
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),  # Endpoint for retrieving, updating, and deleting a user
    path('users/<int:pk>/detail/', UserRetrieveAPIView.as_view(), name='user-retrieve'),  # Endpoint for retrieving a user
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('all/', all_products, name='all_products'),
    path('woman/', woman_products, name='woman_products'),
    path('kids/', kids_products, name='kids_products'),  # Add a new path for kids products
    path('wedding/', wedding_products, name='wedding_products'),  # Add a new path for wedding products
]


