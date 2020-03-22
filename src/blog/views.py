from django.shortcuts import render

# Create your views here.
from blog.models import Post


def all_posts_view(request):
    posts_list = Post.objects.all()
    return render(
        request,
        "blog/index.html",
        {'posts_list': posts_list}
    )


def new_post_view(request):
    return render(
        request,
        "blog/new_post.html",
    )
