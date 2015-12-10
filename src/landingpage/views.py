from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.
def home(request):


	return render(request, "home.html", {})
























