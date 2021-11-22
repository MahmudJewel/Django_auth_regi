from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages

def home(request):
	if request.method == 'POST':
		RegisterForm = SignUpForm(request.POST)
		if RegisterForm.is_valid():
			user = RegisterForm.save()
			user.refresh_from_db()  
			# load the profile instance created by the signal
			user.save()

			# auto sign in
			# raw_password = RegisterForm.cleaned_data.get('password1')
			# login user after signing up
			# user = authenticate(username=user.username, password=raw_password)
			# login(request, user)

			# message passing
			username=RegisterForm.cleaned_data.get('username')
			messages.success(request, f"Account created for {username}")

			# redirect user to home page
			return redirect('/')
	else:
		RegisterForm = SignUpForm()
	context = {
		'RegisterForm' : RegisterForm, 
	}
	return render(request, 'home.html',context)
