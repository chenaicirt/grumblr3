from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from accounts.forms import EditUserProfileForm
from accounts.forms import EditUserForm
from accounts.forms import CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from grumblr_private.models import *
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from accounts.tokens import account_activation_token
from accounts.models import Follower
from django.http import JsonResponse
import json
from django.core import serializers
from django.utils import timezone

import datetime

# Action for the default shared-todo-list/ route.
def index(request):
	all_posts = Post.objects.all().order_by('-date_posted')
	# form = CommentForm()

	#StoreEvent.objects.all().order_by('-date')

    # Gets a list of all the items in the todo-list database.

    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.
	return render(request, 'index.html', {'posts':all_posts})
	

@login_required
def add_comment_to_post(request, pk):

		form = CommentForm(request.POST)

		post = Post.objects.filter(pk=pk).first()

		if request.method == "POST":

			if form.is_valid():
					comment = form.save(commit=False)
					comment.author = request.user
					comment.post = post
					comment.save()
		else:
			form = CommentForm()

		context = {'author': comment.author.username, 'created_date':	comment.created_date, 'text': comment.text, 'post_id': comment.post.id }

		return JsonResponse(context, safe=False)

def change_password(request):
	content = {}

	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return render(request, 'profile.html', content)
		else:
			return render(request, 'change_password.html', content)
	else:
		form = PasswordChangeForm(user=request.user)

		args = {'form': form}
		return render(request, 'change_password.html', args)



def get_user_profile(request):
	context = {}
	all_posts = Post.objects.all().order_by('-date_posted')
	context = {'posts':all_posts, 'user': request.user}

	return render(request, 'profile.html', context)

def get_profile(request,username):
	print(username)
	print ("username")
	if username != "edit": 
		context = {}
		user = User.objects.get(username=username)
		all_posts = Post.objects.all().order_by('-date_posted')
		context = {'posts':all_posts, 'user': user}
		return render(request, 'other_profile.html', context)
	else:
		context = {}
		all_posts = Post.objects.all().order_by('-date_posted')
		context = {'posts':all_posts, 'user': request.user}

		return render(request, 'profile.html', context)

def edit_profile(request):
	content = {}
	profile = request.user.get_username()
	if request.method == 'POST':
		form2 = EditUserForm (request.POST, instance=request.user)
		form = EditUserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
		content['form'] = form
		content['form2'] = form2

		if form.is_valid() and form2.is_valid():
			new_user = form.save()
			new_user2 = form2.save()
			return render(request, 'profile.html', content)

	else:
		form = EditUserProfileForm(instance=request.user)
		form2 = EditUserForm(instance=request.user)
		content['form']= form
		content['form2'] = form2
		return render(request, 'edit_profile.html', content)


def activate(request, uidb64, token):
    context = {}
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration_success.html', context)
    else:
        return render(request, 'registration_fail.html', context)


@login_required 
def add_post(request):
		errors = []  # A list to record messages for any errors we encounter.

		# Adds the new item to the database if the request parameter is present
		if not 'title' in request.POST or not request.POST['title']:
			errors.append('You must enter a post to add.')
		else:
			new_post = Post(title=request.POST['title'], body = request.POST['body'], author = request.user)
			# print("sdflsjflsdjflsdjfslfj")
			# print("NEw POST TIME ZONE")
			# print(new_post.date_posted)
			new_post.save()


		posts = Post.objects.all()

		context = {'posts':posts, 'errors':errors}

		return redirect(index)
		

def check_new_posts(request):
		errors = []  # A list to record messages for any errors we encounter.
		print("hiiii")
		created_time = timezone.now() - timezone.timedelta(seconds=5)
		new_posts = Post.objects.filter(date_posted__gte=created_time)
		# print(new_posts)
		# print(old_posts.all().count())
		# print(Post.objects.all().count())
		return render (request, 'new_posts.html', {"posts": new_posts})

@login_required
def list_followers(request):
	currUser = UserProfile.objects.get(user = request.user)
	follower = Follower.objects.get(current_user=currUser)
	followers = follower.users.all()
	all_posts = Post.objects.all().order_by('-date_posted')

	return render(request, 'follower_field.html', {"followers":followers, "posts": all_posts})


@login_required
def change_followers(request, operation, pk):
	follow = UserProfile.objects.get(pk=pk)
	currUser = UserProfile.objects.get(user = request.user)

	if operation == 'add':
		Follower.make_follower(currUser, follow)
	elif operation == 'remove':
		Follower.remove_follower(currUser, follow)
	return redirect('view_following')