# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpSmall,ExampleForm,ButtonForm,SignIn





def index(request):
	return render(request,'form/nav.html',{'title':'Welcome','page':'welcome'})





def signup_small(request):
	if request.method == 'POST':
		form = 	SignUpSmall(request.POST)
		if form.is_valid():
			try:
				form.save()
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(username=username, password=raw_password)
				if user is not None:
					login(request, user)
					return redirect('form:work_space')
				else:
					return Exception("User is none")
			except Exception as e:
				print e.message
			else:
				return redirect('form:success')
	else:
		form = SignUpSmall()

	return render(request,'form/signup_small.html',{'form':form})






def success(request):
	return HttpResponse("Registered Successfully")





def signin_verify(request):
	print 'in 1'
	if request.method == 'POST':
		print 'in 2'
		form = 	SignIn(request.POST)
		if form.is_valid():
			print 'in 3'
			try:
				print 'in 4'
				username = request.POST['username']
				raw_password = request.POST['password']
				user = authenticate(username=username, password=raw_password)
				if user is not None:
					print 'in 5'
					if user.is_active:
						
						login(request, user)
						return redirect('form:work_space')
					else:
						print 'already logged in'
				else:
					print 'in 6'
					raise Exception("No such user")
			except:
				return HttpResponse('database error')
			else:
				return redirect('form:work_space')
	else:
		form = SignIn()
	return render(request,'form/signin.html',{'form':form})




def signout(request):
	logout(request)
	redirect('form:index')




def work_space(request):
	return render(request,'form/nav.html',{'title':'Work Space','page':'work_space'})







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
		button_form  = ButtonForm(request.POST)
	else:
		small_form = SignUpSmall()
		example_form = ExampleForm()
		button_form = ButtonForm()
	small_form.helper.form_tag = False
	example_form.helper.form_tag = False
	return render(request,'form/multiple_form.html',{'small_form':small_form,'example_form':example_form,'button_form':button_form})