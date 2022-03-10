from django.db import models

# Create your models here.
class Post(models.Model): 
    author = models.CharField(max_length=50, default='Unknown')
    title = models.CharField(max_length=50, default='Unknown')
    content = models.TextField(default='NO content')
