# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import Http404

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.add_message(request, messages.SUCCESS, 'Your account has been created!')
			return render(request, 'users/register.html', {'form': form})
		else:
			messages.add_message(request, messages.ERROR, 'Your account could not be created. Please try again.')
			return render(request, 'users/register.html', {'form': form})

	else:
		form = UserCreationForm
		return render(request, 'users/register.html', {'form': form})


def profile(request, id):
	try:
		user_id = int(id)
		user = User.objects.get(id=user_id)
	except User.DoesNotExist:
		raise Http404("User could not be found")
	return render(request, 'users/profile.html', {'user_id': user_id})