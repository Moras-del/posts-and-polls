from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
from polls.models import Poll
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import remove_perm
from guardian.shortcuts import assign_perm
from django.http import JsonResponse
def home(request):
	return render(request, 'posts/home.html', {'posts': Post.objects.all().order_by('date').reverse()})

@login_required(login_url= 'login')
def newpost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid:
			post = form.save(commit = False)		
			post.owner = request.user
			post.save()
			remove_perm('can_plus_post', post.owner, Post.objects.last())
			return redirect('/')
	else:
		form = PostForm
	return render(request, 'posts/newpost.html', {'form': form})

def post(request, post_id):
	if request.method =='POST':
		form = CommentForm(request.POST)
		if form.is_valid:
			comment = form.save(commit=False)
			comment.author = request.user
			comment.post_id = post_id
			comment.save()
			count = Comment.objects.filter(post__id=post_id).count()
			return render(request, 'posts/post.html', {'count': count,'post': Post.objects.get(id=post_id), 'comments': Comment.objects.filter(post__id=post_id), 'form': form})
	form = CommentForm
	count = Comment.objects.filter(post__id=post_id).count()
	return render(request, 'posts/post.html', {'count': count, 'post': Post.objects.get(id=post_id), 'comments': Comment.objects.filter(post__id=post_id), 'form': form})

def plus(request):
	if request.method == "POST" and request.is_ajax():
		id = request.POST.get('id')
		post = Post.objects.get(id=id)
		post.pluses += 1
		pluses = post.pluses
		post.save()
		return JsonResponse({'pluses': pluses})
