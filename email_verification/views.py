from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import YourEmailVerificationModel
from .serializers import YourEmailVerificationSerializer


class EmailVerificationListCreateAPIView(ListCreateAPIView):
    queryset = YourEmailVerificationModel.objects.all()
    serializer_class = YourEmailVerificationSerializer


class EmailVerificationRetrieveAPIView(RetrieveAPIView):
    queryset = YourEmailVerificationModel.objects.all()
    serializer_class = YourEmailVerificationSerializer


class EmailVerificationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = YourEmailVerificationModel.objects.all()
    serializer_class = YourEmailVerificationSerializer
