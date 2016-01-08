# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    posts = Article.objects.all()
    return render(request, 'articles/home.html', {'posts' : posts})

def detail(request, id):
    try:
        post = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'articles/post.html', {'post' : post})