from django.shortcuts import render
from django.http import Http404


POSTS_AND_ID = {post['id']: post for post in posts}


def post_detail(request, post_id):
    template = 'blog/detail.html'
    try:
        context = {'post': POSTS_AND_ID[post_id]}
    except KeyError:
        raise Http404("Такой страницы не существует")
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)


def index(request):
    template = 'blog/index.html'
    context = {'posts': posts[::-1]}
    return render(request, template, context)
