from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import YourAdminProductsModel
from .serializers import YourAdminProductsSerializer


class AdminProductsListCreateAPIView(ListCreateAPIView):
    queryset = YourAdminProductsModel.objects.all()
    serializer_class = YourAdminProductsSerializer


class AdminProductRetrieveAPIView(RetrieveAPIView):
    queryset = YourAdminProductsModel.objects.all()
    serializer_class = YourAdminProductsSerializer


class AdminProductsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = YourAdminProductsModel.objects.all()
    serializer_class = YourAdminProductsSerializer


# products/views.py
from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})

def woman_products(request):
    woman_products = Product.objects.filter(category='woman')
    return render(request, 'products/woman_products.html', {'woman_products': woman_products})

def kids_products(request):
    kids_products = Product.objects.filter(category='kids')  # Adjust category filter
    return render(request, 'products/kids_products.html', {'kids_products': kids_products})

def wedding_products(request):
    wedding_products = Product.objects.filter(category='wedding')  # Adjust category filter
    return render(request, 'products/wedding_products.html', {'wedding_products': wedding_products})
