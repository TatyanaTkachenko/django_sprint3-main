from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from blog.models import Category, Post

# POSTS_AND_ID = {post['id']: post for post in posts}


def get_posts(all_posts):
    return all_posts.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    template = 'blog/index.html'
    posts = get_posts(Post.objects).order_by('pub_date')[:5]
    context = {'post_list': posts}
    return render(request, template, context)

def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(get_posts(Post.objects), pk=id)
    context = {'post': post}
    return render(request, template, context)

def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_posts(category.posts)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)



