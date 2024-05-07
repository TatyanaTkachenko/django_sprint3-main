from django.db.models.functions import Now
from django.shortcuts import get_object_or_404, render

from . import constants
from .models import Category, Post, User


def get_posts(post_objects, username=None):
    all_published_post = post_objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=Now()
    )
    if username is not None:
        posts_by_username = post_objects.filter(
        author=username
    )
        return all_published_post | posts_by_username
    return all_published_post


def index(request):
    username = request.user
    if request.user.is_anonymous:
        username = None
    template = 'blog/index.html'
    post_list = get_posts(Post.objects, username=username).all()[:constants.POSTS_LIMIT]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    username = request.user
    if request.user.is_anonymous:
        username = None
    template = 'blog/detail.html'
    posts = get_object_or_404(get_posts(Post.objects, username=username).all(), id=post_id)
    context = {'post': posts}
    return render(request, template, context)


def category_posts(request, category_slug):
    username = request.user
    if request.user.is_anonymous:
        username = None
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_posts(category.posts, username).all()
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
