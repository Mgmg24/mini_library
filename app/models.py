from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
 
    
class Book(models.Model):
    pdf = models.FileField(upload_to="pdf",null=True,blank=True)
    book_name=models.CharField(max_length=50,null=True,blank=True)
    auther=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    summary = models.TextField(null=True,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.book_name
    
