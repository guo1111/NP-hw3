from django.shortcuts import render
from django.shortcuts import render_to_response
from django import template
from django.core.context_processors import csrf
# Create your views here.
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate
from trips.models import Data,Account
from datetime import datetime

user = ''

def hello_world(request):
    return render_to_response('hello_world.html',locals())

def login(request):
	global user
	user=''
	c = {}
	c.update(csrf(request))
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	if Account.objects.filter(name=username).exists() :
		L = Account.objects.get(name=username)
		
		user = L.name
		if password == L.pwd :
			if L.name == 'super' :
				return HttpResponseRedirect('/superdata/')
			else :
				return HttpResponseRedirect('/data/')
		else :
			return render_to_response('login.html',c)
	else:
		return render_to_response('login.html',c)
		
def register(request):
	c = {}
	c.update(csrf(request))
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	sex = request.POST.get('sex', '')
	height = request.POST.get('height', '')
	weight = request.POST.get('weight', '')
	hobby = request.POST.get('hobby', '')
	if username=='' or password =='' or sex=='' or height=='' or weight==''or hobby=='':
		return render_to_response('register.html',c)
	else :
		u = Account.objects.create(name = username,pwd=password)
		u.save()
		d = Data.objects.create(name=username,sex=sex,height=height,weight=weight,hobby=hobby,time='0')
		d.save()
		return HttpResponseRedirect('/login/')

def data(request):
	u = Data.objects.get(name=user)
	return render(request,'data.html',{'u': u})
	
def superdata(request):
	u = Data.objects.all()
	return render(request,'superdata.html',{'u': u})
	
def sadd(request):
	c = {}
	c.update(csrf(request))
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	sex = request.POST.get('sex', '')
	height = request.POST.get('height', '')
	weight = request.POST.get('weight', '')
	hobby = request.POST.get('hobby', '')
	if username=='' or password =='' or sex=='' or height=='' or weight==''or hobby=='':
		return render_to_response('sadd.html',c)
	else :
		u = Account.objects.create(name = username,pwd=password)
		u.save()
		d = Data.objects.create(name=username,sex=sex,height=height,weight=weight,hobby=hobby,time='0')
		d.save()
		return HttpResponseRedirect('/superdata/')
	
def sdel(request):
	c = {}
	c.update(csrf(request))
	username = request.POST.get('username', '')
	if username=='' :
		return render_to_response('sdel.html',c)
	else :
		L = Account.objects.get(name=username)
		D = Data.objects.get(name=username)
		L.delete()
		D.delete()
		return HttpResponseRedirect('/superdata/')
	
def modify(request):
	c = {}
	c.update(csrf(request))
	sex = request.POST.get('sex', '')
	height = request.POST.get('height', '')
	weight = request.POST.get('weight', '')
	hobby = request.POST.get('hobby', '')
	if sex=='' or height=='' or weight==''or hobby=='':
		return render_to_response('modify.html',c)
	else :
		u = Data.objects.get(name=user)
		u.sex=sex
		u.height=height
		u.weight=weight
		u.hobby=hobby
		u.time = current_time=datetime.now()
		u.save()
		return HttpResponseRedirect('/data/')