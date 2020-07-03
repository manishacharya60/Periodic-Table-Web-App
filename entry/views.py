from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'entry/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'entry/index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
