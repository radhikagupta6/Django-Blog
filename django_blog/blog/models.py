from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)    
    bio = models.TextField()
    profile_pic = models.ImageField(null= True, blank = True ,upload_to="uploads/prolfile", default='e.png')
    website_url = models.CharField(max_length= 255, null=True, blank=True)
    facebook_url = models.CharField(max_length= 255, null=True, blank=True)
    linkedn_url = models.CharField(max_length= 255, null=True, blank=True)
    twitter_url = models.CharField(max_length= 255, null=True, blank=True)
    github_url = models.CharField(max_length= 255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    
    
class Post(models.Model):
    title = models.CharField(max_length= 255, null=False, blank=False)
    title_tag = models.CharField(max_length= 255)
    snippet = models.CharField(max_length= 255)
    pic = models.ImageField(upload_to="uploads", default='e.png')
    #content = models.TextField(max_length=5000, null=False, blank=False)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blog_post")
    
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')
    
    
    
