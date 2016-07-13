# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.shortcuts import render
from post.models import Post, Categories
from django.shortcuts import redirect
from post.forms import PostForm


def post_like(request, post_id):
    post = Post.objects.get(id=post_id)
    post.like += 1
    post.save()
    return redirect('/')


def post_dislike(request, post_id):
    post = Post.objects.get(id=post_id)
    post.dislike += 1
    post.save()
    return redirect('/')


def post_sort(request, sort_type):
    if sort_type == 'like_asc':
        sort_by = 'like'
    elif sort_type == 'like_desc':
        sort_by = '-like'
    elif sort_type == 'dislike_asc':
        sort_by = 'dislike'
    elif sort_type == 'dislike_desc':
        sort_by = '-dislike'
    else:
        sort_by = 'create_at'
    posts = Post.objects.order_by(sort_by)
    categories = Categories.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'post/post_list.html', context)


def post_list(request):
    posts = Post.objects.all()
    categories = Categories.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_id):
    posts = Post.objects.get(pk=post_id)
    categories = Categories.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'post/post_detail.html', context)


def post_by_category(request, slug):
    try:
        category = Categories.objects.get(slug=slug)
    except Categories.DoesNotExist:
        raise Http404
    context = {
        'category_news': category.post_set.all(),
        'categories': Categories.objects.all(),
    }
    return render(request, 'post/post_by_category.html', context)


def about(request):
    categories = Categories.objects.all()
    return render(request, 'post/about.html', locals())


def contacts(request):
    context = {
        'categories': Categories.objects.all(),
    }
    return render(request, 'post/contacts.html', context)


def create_category(request):
    if 'title' in request.GET and 'slug' in request.GET:
        Categories.objects.create(
            title=request.GET['title'],
            slug=request.GET['slug'],
        )
    context = {
        'categories': Categories.objects.all(),
    }
    return render(request, 'post/create_category.html', context)


def create_post(request):
    categories = Categories.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'post/create_post.html', context)