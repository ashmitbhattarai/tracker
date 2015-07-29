from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth # authentication of users
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt # security against hackers.
from stdpage.models import status1,comment
from stdpage.models import upoad1,asgmnt1
from tracker.forms import upload1Form
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from usermod.models import newuser
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import AnonymousUser
from datetime import date
from stdpage.forms import statusForm
import os

def home(request):
	return render_to_response('index.html')

def login(request):
	c = {} # c is the name of dict file
	c.update(csrf(request))
	return render_to_response('login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request,user)
		#user.is_active = True
		request.session.set_expiry(600)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loggedin(request):
	if request.user == AnonymousUser():
			return HttpResponseRedirect('/accounts/login/')
	
	return render_to_response('dashboard.html',{
			'form':statusForm(),
			'status' : status1.objects.all().order_by('-syear')[:3],
			'asg2': asgmnt1.objects.filter(assignment = True).order_by('doi'),		
			'date1' :date.today(),
			'hits': newuser.objects.filter(user = request.user)[0],
			'files':upoad1.objects.all(),
			'full_name' : request.user.username,
	 		'status2' : status1.objects.all().order_by('-syear')}
	)# might be wrong
@csrf_exempt
def invalid_login(request):
	c = {} # c is the name of dict file
	return render_to_response('invalid_login.html',c)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)	
def logout(request):
	if hasattr(request, 'user'):
	     	request.user = AnonymousUser()
	
	auth.logout(request)
	#[s.delete() for s in Session.Objects.all() if s.get_decoded().get('_auth_user_id')
	#u.is_active = False
	#u.save()	
	request.session.flush()
	
	
	return render_to_response('index.html')

@login_required
def files(request):
	return render_to_response('Window1s.html',{'files1':upoad1.objects.all()})

@login_required	
def files_upload(request):
	if request.POST:
		form = upload1Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/files/')
	else:
		form = upload1Form()
	args = {}
	args.update(csrf(request))
	args['form'] = form		
	return render_to_response('upload_1.html',args) 


def download(request,upoad1_id):
	upload = upoad1.objects.get(id = upoad1_id)
	filename = os.path.basename(upload.thumbnail.name)
	response = HttpResponse(upload.thumbnail)
	response['Content-Disposition'] = 'attachment; filename=%s.iso' % filename

	return response

def contact(request):
	
	return render_to_response ('contacts.html')
@csrf_exempt
def dashboard(request):
	return render_to_response('dashboard.html',{'statuses' : status1.objects.all().order_by('-syear')[0]})
@csrf_exempt
def timeline(request):
	return render_to_response('timeline.html')	

@csrf_exempt
def fileupload(request):
	return render_to_response('fileupload.html')	

@csrf_exempt
def filebrowser(request):
	return render_to_response('filebrowser.html')	
	

@login_required
def search_users(request):
	if request.POST:
		search_text = request.POST['search_text']
	else:
		search_text = ''
	result = status1.objects.filter(name__contains = search_text)
	c = {} # c is the name of dict file
	c.update(csrf(request))
	
	return render_to_response('ajax_search.html',c,{'result':result})	
				
	
