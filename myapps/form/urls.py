from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

app_name = 'form'

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^signup_small/$',views.signup_small,name='signup_small'),
	url(r'^login/$', auth_views.login,{'template_name': 'form/signin.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'form:index'}, name='logout'),
	url(r'^work_space/$',views.work_space,name='work_space'),
	url(r'^multiple_form/$',views.example_multi_form,name='multiple_form'),
	url(r'^success/$',views.success,name='success'),
	url(r'^example_form/$',views.example_form,name='example_form'),

]

