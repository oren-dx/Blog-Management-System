from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    full_name = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f'{self.username}'
    
 
class BlogModel(models.Model):
    CATEGORY_TYPES=[
        ('Educational','Educational'),
        ('Technologies','Technologies'),
        ('Sports','Sports'),
    ]
    
    title = models.CharField(max_length=100,null=True)
    author_name = models.CharField(max_length=100,null=True)
    content = models.TextField(null=True)
    category = models.CharField(choices=CATEGORY_TYPES,max_length=20,null=True)
    blog_image = models.ImageField(upload_to='media/blog_image',null=True)
    publish_date = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    
    
    
    
    
    
    
