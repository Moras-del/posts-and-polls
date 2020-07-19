from django.forms import ModelForm
from .models import Poll, Choices
class PollForm(ModelForm):
	class Meta:
		model = Poll
		labels = {
		'title': 'Poll title'
		}
		fields = ('title',)


class ChoicesForm(ModelForm):
	class Meta:
		model = Choices
		fields = ['choice_text']