from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-id']
    
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'
    

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields='__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    # fields = ['title', 'title_tag', 'content']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')