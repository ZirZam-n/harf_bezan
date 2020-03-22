from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

from .forms import PostForm
from .models import Post


def all_posts_view(request):
    posts_list = Post.objects.all()
    return render(
        request,
        "blog/index.html",
        {'posts_list': posts_list}
    )


def new_post_view(request):
    if request.method == 'GET':
        return render(
            request,
            "blog/new_post.html",
        )
    elif request.method == 'POST':
        print(request.POST)
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('index'))
        return render(
            request,
            "blog/new_post.html",
            {'errors': form.errors},
        )
