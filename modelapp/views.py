from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail

# Create your views here.
from modelapp.forms import CustomerForm
from modelapp.models import Customer, Vendor, Products


def index(request):
    return HttpResponse("this")


def current_page(request):
    form = CustomerForm()
    return render(request, 'customer.html', {'form': form})


def mailsend(request):
    # send_mail("this is ishwar mail", "takecare of your self be safe", "ishwarambare@hotmail.com",
    #           ['ishwarambare@hotmail.com','ishwarambare@gmail.com'],fail_silently=False)
    
    return HttpResponse("mail_will_be_send")
