from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
# Create your views here.
	
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.", extra_tags='text-success')
			return redirect("home:home")
		messages.error(request, "Unsuccessful registration. Invalid information.", extra_tags='text-danger')
	form = NewUserForm()
	return render (request=request, template_name="pages/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.", extra_tags='text-primary')
				return redirect("home:home")
			else:
				messages.error(request,"Invalid username or password.", extra_tags='text-danger')
		else:
			messages.error(request,"Invalid username or password.", extra_tags='text-danger')
	form = AuthenticationForm()
	return render(request=request, template_name="pages/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.", extra_tags='text-primary') 
	return redirect("home:home")