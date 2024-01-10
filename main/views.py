from django.shortcuts import render 
from django.http import HttpResponse
from .models import Food, Reservation, Post, Sign

def index(request):
    return render (request, 'index.html')

def contact(request):
    return render (request, 'contact.html')

def menu(request):
    return render (request, 'menu.html')

def blog(request):
    return render (request, 'blog.html')