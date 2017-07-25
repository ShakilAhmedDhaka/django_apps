from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'form'

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'signup_small/$',views.signup_small,name='signup_small'),
	url(r'multiple_form/$',views.example_multi_form,name='multiple_form'),
	url(r'success/$',views.success,name='success'),
	url(r'example_form/$',views.example_form,name='example_form'),

]

