from django.db import models

class Blogger(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_address=models.EmailField()
    contact_number=models.IntegerField()

    def __str__(self):
        return f'First_name : {self.first_name} Last_name : {self.last_name} Email : {self.email_address} Contact : {self.contact_number}'

class Post(models.Model):
    title=models.CharField(max_length=30)
    date=models.DateTimeField()
    image=models.ImageField(upload_to='images')
    content=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    blogger=models.ForeignKey('Blogger',on_delete=models.CASCADE)

    def __str__(self):
        return f'TItle : {self.title} Date : {self.date} Content : {self.content} image : {self.image}'



