# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.core.context_processors import csrf
from django import forms
from django.db.models import Q

from blog.models import Post, Tag

from datetime import datetime


# Create your views here.
class PostForm(forms.Form):
	title = forms.CharField(max_length=100, error_messages={'required': 'Please enter your name'})
	content = forms.CharField(widget=forms.Textarea, error_messages={'required': 'Please enter content'})
	tags = forms.CharField(max_length=100, required=False)


def Index(request):
	if request.POST:
		if not request.user.is_authenticated():
			return redirect('/login/')
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
	posts = Post.objects.all().order_by('-pub_date')
	tags = Tag.objects.all()
	post_form = PostForm()
	ctx.update(csrf(request))
	ctx['posts'] = posts
	ctx['tags'] = tags
	ctx['form'] = post_form
	return render(request, 'blog/index.html', ctx)


def Archive(request):
	ctx = {}
	post_titles = Post.objects.all().order_by('-pub_date')
	ctx['post_titles'] = post_titles
	return render(request, 'blog/archive.html', ctx) 


def Show_post(request, post_id):
	ctx = {}
	a_post = Post.objects.get(id=post_id)
	ctx.update(csrf(request))
	ctx['a_post'] = a_post
	return render(request, 'blog/blog.html', ctx)

def Search(request):
	# name = request.POST.get('search',None)
	# if name:
	# 	extra_context = {'searchvalue':name}
	# 	return object_list(request, Post.objects.filter('content__contains':name), paginate_by=10, extra_context=extra_context)
 #  	else:
 #    	return redirect('/')
 	if 'q' in request.GET:
 		term = request.GET['q']
 		post_list = Post.objects.filter(Q(title__icontains=term) | Q(content__icontains=term))
 		ctx = {}
 		ctx['post_list'] = post_list
 		# return render(request, 'blog/search.html', ctx)
 		return render_to_response('blog/search.html', locals())