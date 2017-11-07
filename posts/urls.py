from django.conf.urls import url, include

from . import views

app_name = 'posts'
urlpatterns = [
	url(r'^submit_post/$', views.submit_post, name='submit_post'),
	url(r'^$', views.index, name='index'),
]
