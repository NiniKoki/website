from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import YourUsersModel
from .serializers import YourUsersSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


class UserListCreateAPIView(ListCreateAPIView):
    queryset = YourUsersModel.objects.all()
    serializer_class = YourUsersSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = YourUsersModel.objects.all()
    serializer_class = YourUsersSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = YourUsersModel.objects.all()
    serializer_class = YourUsersSerializer


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
