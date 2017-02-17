from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm

def home(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form_name = form.cleaned_data['name']
			form_email = form.cleaned_data['email']
			form_message = form.cleaned_data['message']
			subject = 'Contato Site DefOS'
			from_email = settings.EMAIL_HOST_USER
			to_email = [from_email]
			contact_message = 'Mensagem recebida de %s: \n\n%s \n\nvia %s'%(form_name, form_message, form_email)
			send_mail(subject, 
		 		contact_message,
		 		from_email,
		 		to_email,
			 	fail_silently=True)
			return redirect('thankyou')
	else:
		form = ContactForm()
	return render(request, "index.html", {'form': form})

def thankyou(request):
	return render_to_response('thankyou.html')
	

