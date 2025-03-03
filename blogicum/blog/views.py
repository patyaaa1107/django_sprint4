import datetime

from django.shortcuts import get_object_or_404, render

from .models import Category, Post
from .constants import LIMITOFPOSTS


def index(request):
    template_name = "blog/index.html"
    posts = Post.objects.filter(
        is_published__exact=True,
        pub_date__lt=datetime.datetime.now(),
        category__is_published=True,
    ).order_by(
    )[:LIMITOFPOSTS]
    context = {"posts": posts}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = "blog/detail.html"
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        pub_date__lt=datetime.datetime.now(),
        category__is_published=True,
    )
    context = {"post": post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lt=datetime.datetime.now()
    )
    context = {"category_slug": category_slug, "posts": posts}
    return render(request, "blog/category.html", context)
