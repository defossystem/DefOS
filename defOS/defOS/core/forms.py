from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
	name = forms.CharField(label="Name", max_length=50)
	# subject = forms.CharField(required=True)
	email = forms.EmailField(label='E-mail')
	message= forms.CharField(label='Mensagem', widget=forms.Textarea)

