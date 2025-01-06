from django import forms
from .models import Post
class ViewPost(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','date','image','content','description','blogger']