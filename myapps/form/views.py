# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


from django.db import transaction
from .forms import SignUpSmall,ExampleForm,ButtonForm,SignIn, ProfileForm


from django.contrib.auth.decorators import login_required

from django.http import JsonResponse



def index(request):
	return render(request,'form/welcome.html',{'title':'Welcome','page':'welcome'})




def signup_small(request):
	if request.method == 'POST':
		form = 	SignUpSmall(request.POST)
		if form.is_valid():
			try:
				form.save()
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password1')
				print form.cleaned_data.get('username')
				print form.cleaned_data.get('email')
				user = authenticate(username=username, password=raw_password)
				if user is not None:
					login(request, user)
					return redirect('form:work_space')
				else:
					raise Exception("User is none")
			except Exception as e:
				print e.message
			else:
				return redirect('form:success')
	else:
		form = SignUpSmall()

	return render(request,'form/signup_small.html',{'form':form})






@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
    	print request.user
    	user_form = SignUpSmall(request.POST, instance=request.user)
    	profile_form = ProfileForm(request.POST, instance=request.user.profile)
    	if user_form.is_valid():
        	user_form.save()
        	messages.success(request, _('Your profile was successfully updated!'))
        else:
        	user_form = SignUpSmall(instance=request.user)
        	messages.error(request, _('Please correct the error below.'))
    	if profile_form.is_valid():
			profile_form.save()
			messages.success(request, _('Your profile was successfully updated!'))
    	else:
    		profile_form = ProfileForm(instance=request.user.profile)
        	messages.error(request, _('Please correct the error below.'))
    else:
        user_form = SignUpSmall(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'form/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })






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
	return render(request,'form/work_space.html',{'title':'Work Space','page':'work_space'})







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
	
	
	
# helper methods for ajax calls

def check_get_user(request):
    username = request.GET.get('username', None)
    print username
    
    valid = False
    email = 'Email'
    contact = 'Contact'
    address = 'Address'
    birth_date = 'Date of Birth'
    password = ''
    
    if User.objects.filter(username__iexact=username).exists():
    	valid = True
    	user = User.objects.get(username=username)
    	email = user.email
    	if user.profile.contact is not '':
    		contact = user.profile.contact
    	if user.profile.location is not '':
    		address = user.profile.location
    	if user.profile.birth_date is not None:
    		birth_date = user.profile.birth_date

    	
    data = {
        'valid': valid,
        'email': email,
        'contact':contact,
        'address':address,
        'birth_date':birth_date
    }
    
    
    return JsonResponse(data)