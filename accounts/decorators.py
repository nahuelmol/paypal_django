from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):

	def wrapper_function(req, *args, **kwargs):
		if req.user.is_authenticated:
			return redirect('home')
		else:
			return view_function(req, *args, **kwargs)

	return wrapper_function

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper(req,*args,**kwargs):
			group = None

			if req.user.groups.exists():
				#the next line just extract the name of the first group, which one the user is member
				group = req.user.groups.all()[0].name

				print(group)
			if group in allowed_roles:
				return view_func(req, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized')
			
		return wrapper
	return decorator