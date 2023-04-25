from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
from .forms import *
from datetime import datetime


# Create your views here.
def adminLoginView(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user_obj = User.objects.filter(username = username)

		if not user_obj.exists():
			messages.warning(request, 'Account not found ')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		user_obj = authenticate(username = username , password = password)

		if user_obj and user_obj.is_superuser:
			login(request ,user_obj)
			return redirect('/adminmainpage/')

		messages.info(request,'invalid password')
		return redirect('/invalidcredentials1/')

	return render(request,'adminLogin.html')

def adminmainpageView(request):
	if request.method =="POST":
		form=videoDetailsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/completed/')
	else:
		form=videoDetailsForm()
	return render(request,'adminmainpage.html',{'form':form})



def invalidcredentials1(request):
	return render(request,'invalidcredentials1.html')

def completed(request):
	return render(request,"completed.html")
