# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post, Tag

# Register your models here.
class TagInline(admin.TabularInline):
	model = Tag

class PostAdmin(admin.ModelAdmin):
	""" Inline Display """
	inlines = [TagInline]

admin.site.register(Post, PostAdmin)