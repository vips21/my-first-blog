# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,loader,get_object_or_404
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Blog/post_detail.html', {'post': post})