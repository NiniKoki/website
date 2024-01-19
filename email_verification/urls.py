from django.urls import path
from .views import (
    EmailVerificationListCreateAPIView,
    EmailVerificationRetrieveAPIView,
    EmailVerificationRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('email-verifications/', EmailVerificationListCreateAPIView.as_view(), name='email-verification-list'),  # List and create email verifications
    path('email-verifications/<int:pk>/', EmailVerificationRetrieveAPIView.as_view(), name='email-verification-detail'),  # Retrieve a specific email verification
    path('email-verifications/<int:pk>/update/', EmailVerificationRetrieveUpdateDestroyAPIView.as_view(), name='email-verification-update-delete'),  # Retrieve, update, or delete a specific email verification
    # Add other email verification-related URLs as needed
]
