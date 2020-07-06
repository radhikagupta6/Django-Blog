from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Radhika Gupta',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 27,2020'

    },
    {
        'author': 'Prakhar Gupta',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 28,2020'

    }
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': "About"})
