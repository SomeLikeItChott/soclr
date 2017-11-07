# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from model_utils.managers import InheritanceManager


class Post(models.Model):
	user = models.ForeignKey(User, editable = False)
	time = models.DateTimeField(auto_now=True)
	objects = InheritanceManager()


class TextPost(Post):
	content = models.TextField()

