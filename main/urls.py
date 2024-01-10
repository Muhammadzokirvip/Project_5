from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('menu', menu, name='menu'),
]