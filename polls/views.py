from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, DetailView, ListView
import matplotlib.pyplot as plt
import matplotlib
from .models import Poll, Choice


class VoteView(DetailView):
	pk_url_kwarg = "pk"
	model = Poll
	template_name = "polls/poll-detail.html"
	context_object_name = "poll"

	def post(self, *args, **kwargs):
		choice_id = self.request.POST['choice']
		choice = get_object_or_404(Choice, pk=choice_id)
		choice.newvote()
		choice.save()
		return redirect(reverse("polls:result", args=[choice.poll.id]))

class PollsList(ListView):
	model = Poll
	template_name = "polls/list.html"
	context_object_name = "polls"



def result(request, poll_id):
	poll = get_object_or_404(Poll, id=poll_id)
	array = [choice.votes for choice in poll.choices.all()]
	labels = [choice.text for choice in poll.choices.all()]
	matplotlib.use("Agg")
	fig1, ax1 = plt.subplots()
	ax1.pie(array, labels=labels, autopct='%1.0f%%')
	fig1.savefig('media/images/model{}.png'.format(poll_id))
	return render(request, 'polls/result.html', {"poll": poll})

class CreatePollView(View):

	def get(self, request):
		return render(request, "polls/newpoll.html")

	def post(self, request):
		title = request.POST['title']
		choices = request.POST.getlist('choice')
		poll = Poll()
		poll.title = title
		poll.save()
		choices_objs = [Choice(poll=poll, text=text) for text in choices]
		Choice.objects.bulk_create(choices_objs)
		return redirect(reverse("polls:list"))

