from django.shortcuts import render
from .models import Blogger,Post
from blogapp.forms import ViewPost
from django.http import HttpResponse
import os


# Create your views here.

def home(request):
    bloggers=Blogger.objects.all()
    posts=Post.objects.all()
    return render(request,"blogapp/index.html",{"blogger":bloggers,"post":posts})


def post(request):
    posts=Post.objects.all()
    return render(request,"blogapp/register.html",{"post":posts})

def ViewPostList(request):
        if request.method == 'POST':
           form = ViewPost(request.POST)
           if form.is_valid():
               print(form.cleaned_data)
               return HttpResponse('thank you')
        else:
           form = ViewPost()

    # posts=ViewPost()
        return render(request,"blogapp/form.html",{"form":form})