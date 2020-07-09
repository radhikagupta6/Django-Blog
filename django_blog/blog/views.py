from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,DetailView, CreateView
from .forms import PostForm
class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'
    

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields='__all__'