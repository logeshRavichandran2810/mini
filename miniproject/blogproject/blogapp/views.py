from django.shortcuts import render,HttpResponse,redirect
from .models import Blogger,Post
from django.views.generic import ListView
from blogapp.forms import PostForm


# Create your views here.

def home(request):
    bloggers=Blogger.objects.all()
    posts=Post.objects.all()
    return render(request,"blogapp/index.html",{"blogger":bloggers,"post":posts})


def post(request):
    posts=Post.objects.all()
    return render(request,"blogapp/register.html",{"post":posts})

def PostViewList(request):
    # posts=Post.objects.all()
    form=PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('post')
        else:
            form=PostForm()
        return render(request,"blogapp/form.html",{"form":form})
    return render(request,"blogapp/form.html",{"form":form})
            


