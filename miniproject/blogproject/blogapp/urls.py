from django.urls import path
from blogapp.views import home
from blogapp.views import post
from blogapp.views import PostViewList
from .import views

urlpatterns= [
    path('home/',views.home,name='home'),
    path('post/',views.post,name='post'),
    path('post/Add/',views.PostViewList,name='PostViewList')
]