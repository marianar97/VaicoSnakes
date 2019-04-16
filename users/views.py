from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):

    return render(request, 'users/login.html')