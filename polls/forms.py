from django.forms import ModelForm, BaseForm
from django import forms
from .models import Poll, Choice


class PollForm(forms.Form):
	title = forms.CharField(max_length=200)
	choices = forms.CharField()

