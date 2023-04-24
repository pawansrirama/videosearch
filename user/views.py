from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .forms import *
from .models import *
from myadmin.views import *


def usersignupView(request):
	if request.method == 'POST':
		emailAddress = request.POST.get('emailAddress')
		password = request.POST.get('password')
		user_obj = registerDetials.objects.filter(emailAddress = emailAddress).first()

		if user_obj is not None and user_obj.password == password and user_obj.emailAddress == emailAddress:
			return redirect('mainpage/')
		else:
			return redirect('invalidcredentials/')

	return render(request,'usersignup.html')

def registerView(request):
	if  request.method=="POST":
		form=registerDetialsForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect(reverse('usersignup'))
	else:
		form=registerDetialsForm()
	return render(request,'register.html',{'form':form})


def invalidcredentials(request):
	return render(request,'loginAgain.html')

def mainpage(request):
	video_details=videoDetails.objects.all()
	return render(request,'mainpage.html',{'video_details':video_details})


def details_video_View(request,id):
	video = videoDetails.objects.get(id=id)

	allvideo = videoDetails.objects.all()
	return render(request,'details_video_View.html',{'video':video,'allvideo':allvideo})

def aboutusView(request):
	return render(request,'aboutus.html')

def contactView(request):
	return render(request,'contact.html')




