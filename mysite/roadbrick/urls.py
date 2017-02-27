from django.conf.urls import  url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'$', views.post_load, name='post_load'),
	]
