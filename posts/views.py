# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from posts.forms import TextPostForm
from posts.models import *
from django.contrib import messages
from django.urls import reverse


def index(request):
	if request.user.is_authenticated:
		textForm = TextPostForm()
		posts = Post.objects.all().select_subclasses()
		return render(request, 'posts/feed.html', {'textForm': textForm, 'posts': posts})
	else:
		return render(request, 'index-preview.html')

def submit_post(request):
	if request.method == 'POST':
		post_form = TextPostForm(request.POST)
		if post_form.is_valid():
			post = post_form.save(commit=False)
			post.user = request.user
			print(post.content)
			post.save()
			messages.success(request, 'Your post has been posted.')
			return redirect('/')
		else:
			messages.success(request, 'Bad post op.')
			return redirect('/')
