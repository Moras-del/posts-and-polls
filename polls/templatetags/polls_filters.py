from django import template


register = template.Library()

@register.filter
def mean(a,b):
	try:
		var = int((a/b)*100)
	except ZeroDivisionError:
		var = 0
	return var