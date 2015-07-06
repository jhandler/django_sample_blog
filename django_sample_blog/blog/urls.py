from django.conf.urls import patterns, include, url
 
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
        url(r'^$', 'blog.views.index',name='blog-index'),
    #    url(r'^post/(?P<pk>\d+)$', 'blog.views.blog_post', name='blog-post'),
)