from django.forms import ModelForm
from .models import Poll, Choices
class PollForm(ModelForm):
	class Meta:
		model = Poll
		labels = {
		'num_of_choices': 'Number of choices'
		}
		fields = ['title','num_of_choices']


class ChoicesForm(ModelForm):
	class Meta:
		model = Choices
		fields = ['choice_text']