from django.db import models
from datetime import datetime  
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150, default='')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "categories"

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    title = models.CharField(max_length=150)
    description = models.TextField(default='')
    content = models.TextField(default='')
    image = models.FileField(default='', blank=True)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} - {1}'.format(self.id, self.title)