from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
	url(r'^$', 'blog.views.Index'),
	url(r'^archive/$', 'blog.views.Archive'),
	url(r'^blog/(?P<post_id>\d*)', 'blog.views.Show_post'),												
)				

