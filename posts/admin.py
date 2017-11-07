# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from posts.models import Post, TextPost

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	readonly_fields=('time',)

@admin.register(TextPost)
class TextPostAdmin(admin.ModelAdmin):
	readonly_fields=('time',)
