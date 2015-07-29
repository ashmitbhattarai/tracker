from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth # authentication of users
from django.core.context_processors import csrf # security against hackers.
from usermod.forms import newuserForm
from django.contrib.sessions.models import Session
from usermod.models import newuser
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model
from usermod.forms import user_updateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def reg_success(request):
	return render_to_response('regcomplete.html')
	
def user_register(request):	
	if request.POST:
		form = newuserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/makeuser/reg_success/')
	else:
		form =newuserForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	
	return render_to_response('register.html',args)
@login_required	
def user_update(request):
	if request.POST:
		form = user_updateForm(request.POST,request.FILES,instance=request.user.profile)
		if form.is_valid():
			a = form.save(commit = False)
			
			a.save()
			return HttpResponseRedirect('/accounts/loggedin/')
	else:
		user = request.user
		profile = user.profile
		form  = user_updateForm(instance = profile)
	args = {}
	args.update(csrf(request))
	args['form'] = form
		
	return render_to_response('info_update.html',args)

"""@login_required	
def asg_reg(request):
	if request.POST:
		form = asg_Form(request.POST, instance = request.user.profile)
		if form.is_valid():
			f = form.save(commit = False)
			
			f.save()
			return HttpResponseRedirect('/accounts/loggedin/')
	else:
		user = request.user
		profile = user.profile
		form = asg_Form(instance = profile)
	args = {}
	args.update(csrf(request))
	args['form'] = form
	
	return render_to_response('asgmnt.html',args)"""
