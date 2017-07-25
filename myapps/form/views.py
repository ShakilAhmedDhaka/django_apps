# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User

from .forms import SignUpSmall,ExampleForm,ButtonForm


def index(request):
	return HttpResponse('welcome')


def example_form(request):
	if request.method == 'POST':
		form = ExampleForm(request.POST)
	else:
		form = ExampleForm()
	return render(request,'form/signup_small.html',{'form':form,'helper':form.helper})
				

def example_multi_form(request):
	if request.method == 'POST':
		small_form = SignUpSmall(request.POST)
		example_form = ExampleForm(request.POST)
	else:
		small_form = SignUpSmall()
		example_form = ExampleForm()
		button_form = ButtonForm()
	small_form.helper.form_tag = False
	example_form.helper.form_tag = False
	return render(request,'form/multiple_form.html',{'small_form':small_form,'example_form':example_form,'button_form':button_form})



def signup_small(request):
	if request.method == 'POST':
		form = 	SignUpSmall(request.POST)
		if form.is_valid():
			try:
				user=User()           
				user.first_name=request.POST['first_name']
				user.last_name=request.POST['last_name']
				user.user_id=request.POST['user_id']
				user.email_id=request.POST['email_id']
				user.password=request.POST['passwd']
				user.save()
			except:
				return HttpResponse('failed')
			else:
				return HttpResponseRedirect("success")
	else:
		form = SignUpSmall()
	

	return render(request,'form/signup_small.html',{'form':form})


def success(request):
	return HttpResponse("Registered Successfully")


