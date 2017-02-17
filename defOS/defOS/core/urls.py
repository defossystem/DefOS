from django.conf.urls import url
from django.conf.urls.static import static
from defOS.core import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^thankyou/$', views.thankyou, name='thankyou'),
]