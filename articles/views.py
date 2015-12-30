# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    post_list = Article.objects.all()
    return render(request, 'articles/home.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'articles/post.html', {'post' : post})