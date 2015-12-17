from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^Juan/', views.juanpage, name ='juanpage'),
	url(r'^$', views.index, name ='index'),	
]