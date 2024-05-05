from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def get_posts():
    return Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    )


def index(request):
    template = 'blog/index.html'
    post_list = get_posts().order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    posts = get_object_or_404(get_posts(), id=id)
    context = {'post': posts}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_posts().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
