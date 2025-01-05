from django.shortcuts import render
from .models import Blogger,Post


# Create your views here.

def home(request):
    bloggers=Blogger.objects.all()
    posts=Post.objects.all()
    return render(request,"blogapp/index.html",{"blogger":bloggers,"post":posts})


def register(request):
    return render(request,"blogapp/register.html")


