# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
from django import forms

from blog.models import Post, Tag

from datetime import datetime


# Create your views here.
class PostForm(forms.Form):
	title = forms.CharField(max_length=100, error_messages={'required': 'Please enter your name'})
	content = forms.CharField(widget=forms.Textarea, error_messages={'required': 'Please enter content'})
	tags = forms.CharField(max_length=100, required=False)


def Index(request):
	if request.POST:
		form = PostForm(request.POST)
		if form.is_valid():
			submitted_title = request.POST['title']
			submitted_content = request.POST['content']
			submmited_tags = request.POST['tags']
			pub_date = datetime.now()
			new_post = Post(title=submitted_title, 
							content=submitted_content, pub_date=pub_date)
			new_post.save()
			submmited_tags = submmited_tags.replace('，', ',')
			tags = submmited_tags.split(',')
			for tag in tags:
				tag.strip()
				new_tag = Tag(post=new_post, name=tag)
				new_tag.save()
	""" request.GET """
	ctx = {}
	posts = Post.objects.all()
	tags = Tag.objects.all()
	post_form = PostForm()
	ctx.update(csrf(request))
	ctx['posts'] = posts
	ctx['tags'] = tags
	ctx['form'] = post_form
	return render(request, 'blog/index.html', ctx)


def Archive(request):
	ctx = {}
	post_titles = Post.objects.all()
	ctx['post_titles'] = post_titles
	return render(request, 'blog/archive.html', ctx) 
