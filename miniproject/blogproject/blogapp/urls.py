from django.urls import path
from blogapp.views import home
from blogapp.views import register
from .import views

urlpatterns= [
    path('home/',views.home),
    path('register/',views.register)
]