from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from .forms import PostForm, RegistrationForm
from .models import Post
# Create your views here.
#Actually this is the controller part of the project

@login_required
def home(request):
	context = {}
	if request.method == 'POST':
		new_post = PostForm(request.POST)
		if new_post.is_valid():
			#print new_post.cleaned_data['title']
			#Need to add user info to current post, otherwise will throw out error. But why?
			instance = new_post.save(commit=False)
			instance.user = request.user
			instance.save()

	post_list = Post.objects.filter(user=request.user)
	context['post_list'] = post_list

	return render(request, 'post_list.html', context)




@transaction.atomic
def register(request):
	context={}

	if request.method == 'GET':
		context['form'] = RegistrationForm()
		#return render(request, 'register.html', context_instance=RequestContext(request, context))
		return render(request, 'register.html', context)

	form = RegistrationForm(request.POST)

	context['form'] = form
	
	if not form.is_valid(): #This method is to validate all the clean function in the forms.py file.
		#return render(request, 'register.html', context_instance=RequestContext(request, context))
		return render(request, 'register.html', context)

	print form.cleaned_data['username']
	new_user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
	#new_user = User.objects.create_user('John', 'pwd', 'abc@gmail.com')
	new_user.save()

	new_user = authenticate(username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'])

	login(request, new_user)
	return redirect('/blog/')




@login_required
def post_create(request):
	context = {}
	context['form'] = PostForm()
	return render(request, 'post_form.html', context)


def post_delete(request):

	return HttpResponse("<h1>Hello World Delete</h1>")

def post_update(request):

	return HttpResponse("<h1>Hello World Update</h1>")


def post_detail(request):
	context = {}

	
	return render(request, "post_list.html", context)


def post_list(request):
	context = {}


	return render(request, "post_list.html", context)