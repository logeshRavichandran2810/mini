from django.contrib import admin
from .models import Blogger,Post

# Register your models here
class blogadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email_address','contact_number')
class postadmin(admin.ModelAdmin):
    list_display=('title','date','content')
admin.site.register(Blogger,blogadmin)
admin.site.register(Post,postadmin)