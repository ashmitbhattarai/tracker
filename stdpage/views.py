from django.shortcuts import render_to_response
from stdpage.models import stdpage
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth # authentication of users
from django.core.context_processors import csrf # security against hackers.
from django.utils import timezone
from stdpage.models import status1, comment,asgmnt1
from stdpage.forms import statusForm,commentForm,asg1_Form
from django.contrib.auth.decorators import login_required
from datetime import date,timedelta
from django.views.decorators.csrf import csrf_exempt # security against hackers.


def stdpages(request):
	return render_to_response('stdpages.html',
				{'stdpage': stdpage.objects.all() })

def stdlist(request,stdpage_id=1):
	return render_to_response('stdlist.html',
				{'stdlist':stdpage.objects.get(id=stdpage_id)}) 

@csrf_exempt
@login_required
def create(request):
	if request.POST:
		form = statusForm(request.POST)
		if form.is_valid():
			c = form.save(commit = False)
			c.user1 = request.user.username
			c.save()
			return HttpResponseRedirect('/accounts/loggedin')
	else:
		form = statusForm()
	args = {}
	args['form'] = form		
	return render_to_response('create_form.html',args) # might be wrong
	
@login_required	
def asg1_reg(request):
	if request.POST:
		form = asg1_Form(request.POST)
		if form.is_valid():
			f = form.save(commit = False)
			f.user = request.user.username
			f.save()
			return HttpResponseRedirect('/accounts/loggedin/')
	else:
		
		form = asg1_Form()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	
	return render_to_response('asgmnt.html',args)

@login_required
def add_comment(request,status1_id): # status ko id resepective status ma pass garnu paryo...
	a = status1.objects.get(id = status1_id)
	if request.POST:
		f= commentForm(request.POST)
		if f.is_valid:
			c = f.save(commit = False)
			c.user_1 = request.user.username
			c.Status1 = a
			c.save()
			return HttpResponseRedirect('/accounts/loggedin/')
	else:
		f= commentForm()	
	args = {}
	args.update(csrf(request)) # to check if the form is valid
	args['Status1'] = a
	args['form'] = f
	return render_to_response('add_comment.html',args)
@login_required	
def show_asgmnt(request):
	a = asgmnt1.objects.filter(user__contains = request.user.username)
	
	return render_to_response('asgmnt_see.html',{'asg_notify':a,'date2' :date.today()})

@login_required	
def not_show(request,asgmnt1_id):
	a = asgmnt1.objects.get(id = asgmnt1_id)
	a.submitted = True
	a.save()
	return HttpResponseRedirect ('/stdpages/show/')
	

