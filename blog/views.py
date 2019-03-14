from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author':'jess',
        'title': 'testing',
        'content': 'first post',
        'date_posted': 'today'
    },
    {
        'author': 'jane doe',
        'title': 'test 2',
        'content': 'I hope you like this blog',
        'date_posted': 'march 13th'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

def about(request):
      return render(request, 'blog/about.html', {'title': 'About'})