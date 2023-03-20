from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category
    

class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to='news/images')
    published_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    uploaded_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default='DF'
        )
    
    def __str__(self):
        return self.title
    
    