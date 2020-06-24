from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from modelapp.forms import CustomerForm
from modelapp.models import Customer, Vendor, Products


def index(request):
    return HttpResponse("this")


def current_page(request):

    form = CustomerForm()
    return render(request,'customer.html',{'form': form})


def mailsend(request):
    return HttpResponse("mail_will_be_send")