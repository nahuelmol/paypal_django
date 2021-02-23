from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserForm

def registerPage(req):
	form = UserForm()

	if req.method == 'POST':
		form = UserForm(req.POST)
		print(form)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			print(password)
			messages.success(req,'Account was created for {}'.format(user))

			return redirect('login')

	context = {'form':form}
	
	return render(req,'accounts/register.html',context)

def loginPage(req):
	

	if req.method == 'POST':
		username = req.POST.get('username')
		password = req.POST.get('password')

		print(username)
		print(password)

		user = authenticate(req,username=username,password=password)

		if user is not None:
			login(req,user)
			return redirect('home')
		else:
			messages.info(req,'username or password is incorrect!')
	
	context = {}

	return render(req,'accounts/login.html',context)

def Home(req):
	return render(req,'accounts/home.html')