from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.mail import send_mail

# Create your views here.
from modelapp.forms import CustomerForm
from modelapp.models import Customer, Vendor, Products


def index(request):
    return HttpResponse("this")


def current_page(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            order = form.cleaned_data['order']
            email = form.cleaned_data['email']
            user = form.cleaned_data['user']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            print(name)
            send_mail("Hi"+name+"this is from NEXTCLICK", "your" + order + "is ready for dispatch\nthank you for your shopping|||", "ambareishu@gmail.com",
                      ['ishwarambare@hotmail.com', 'ishwarambare@gmail.com'], fail_silently=False)
            form.save()
            redirect(mailsend)
    else:
        form = CustomerForm()
        return render(request, 'customer.html', {'form': form})


def mailsend(request):
    send_mail("this is from NEXTCLICK", "your car is ready for dispatch\nthank you for your shopping", "ambareishu@gmail.com",
              ['ishwarambare@hotmail.com', 'ishwarambare@gmail.com'], fail_silently=False)

    return HttpResponse("mail_will_be_send_check_your_mail_please_thank_you_for_shopping_have_a_good_day_ahead")
    # return render(request, 'mailsend.html', {'data': data})
