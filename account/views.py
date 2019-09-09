from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout as user_logout
from posts.models import Post
from polls.models import Poll, Choices
from guardian.shortcuts import assign_perm
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			user = User.objects.last()
			assign_perm('can_vote_poll', user, Poll.objects.all())
			assign_perm('can_plus_post', user, Post.objects.all())
			import cv2
			import os
			cam = cv2.VideoCapture(0)
			path = "media/images"
			ret, frame = cam.read()
			k = cv2.waitKey(1)
			img_name = "opencv_frame_{}.png".format(user.id)
			cv2.imwrite(os.path.join(path, img_name), frame)
			cam.release()
			return render(request, 'account/registered.html')
	else:
		form = UserCreationForm()
	return render(request, 'account/register.html',{'form':form})

def logout(request):
	user_logout(request)
	return render(request, 'account/logout.html')

def profile(request):
	if request.method == 'POST':
		post_id = request.POST.get('delete', False)
		if post_id:
			Post.objects.get(id = post_id).delete()
		poll_id = request.POST.get('deletepoll', False)
		if poll_id:
			Poll.objects.get(id=poll_id).delete()
		return render(request, 'account/profile.html', {'posts': Post.objects.filter(owner = request.user), 'polls': Poll.objects.filter(owner = request.user)})

	else:
		return render(request, 'account/profile.html', {'posts': Post.objects.filter(owner = request.user), 'polls': Poll.objects.filter(owner = request.user)})
# Create your views here.
