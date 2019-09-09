from django.shortcuts import render, redirect
from .forms import PollForm, ChoicesForm
from .models import Poll, Choices
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import remove_perm
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm


@login_required(login_url='login')
def vote(request,poll_id):
	if request.user.has_perm('can_vote_poll', Poll.objects.get(id = poll_id)):
		if request.method == 'POST':
			choice = int(request.POST['choice'])
			obj = Choices.objects.get(id = choice)
			obj.newvote()
			poll = Poll.objects.get(id = poll_id)
			poll.new_total_vote()
			poll.save()
			obj.save()
			remove_perm('can_vote_poll', request.user, Poll.objects.get(id = poll_id))
			return redirect('result', poll_id = poll_id)
		else:
			return render(request, 'polls/polls.html',{'polls': Poll.objects.get(id = poll_id), 'choices': Choices.objects.filter(poll__id = poll_id)})
	else:
		return redirect('result', poll_id = poll_id)

def polls(request):
	return render(request, 'polls/seepolls.html',{'polls':Poll.objects.all().order_by('date').reverse()})

	
def result(request, poll_id):
	poll = Poll.objects.get(id = poll_id)
	choices = Choices.objects.filter(poll__id = poll_id)
	var = 0
	arr = []
	labels = []
	for choice in choices:
		var += choice.votes
		arr.append(choice.votes)
		labels.append(choice.choice_text)
	form = {
	'poll': poll,
	'choices': choices,
	'var': var
	}
	import matplotlib.pyplot as plt
	fig1, ax1 = plt.subplots()
	ax1.pie(arr, labels = labels,autopct='%1.0f%%')
	fig1.savefig('media/images/model{}.png'.format(poll_id))
	return render(request, 'polls/result.html', form)


@login_required(login_url='login')
def newpoll(request):
	if request.method =='POST':
		form = PollForm(request.POST)
		if form.is_valid:
			poll = form.save(commit=False)
			poll.owner = request.user
			poll.save()
			assign_perm('can_vote_poll', User.objects.all(), Poll.objects.last())
			return redirect('choices',id = poll.id)
	else:
		form = PollForm

	return render(request, 'polls/newpoll.html', {'form': form})


@login_required(login_url='login')
def newpollchoices(request, id):
	poll = Poll.objects.get(id = id)
	num = poll.num_of_choices
	form = [None] * num
	arr = [None] * num
	if request.method=='POST':
		for j in range(0, len(arr)): 
			form[j] = ChoicesForm(request.POST, prefix="form{}".format(j))
			if form[j].is_valid:
				choices = form[j].save(commit=False)
				choices.poll_id = id
				choices.save()
		return redirect('home')
	else:
		for i in range(0, len(arr)):
			form[i] = ChoicesForm(prefix="form{}".format(i))
	return render(request, 'polls/choices.html', {'form': form, 'poll': poll, 'num': num, 'arr': arr})