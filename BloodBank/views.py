from django.shortcuts import render, HttpResponse, redirect


import os
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'BloodBank/home.html')