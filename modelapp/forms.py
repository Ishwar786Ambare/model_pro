from django import forms
from modelapp.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'



# class CustomerForm(forms.Form):
#     order = forms.CharField(max_length=100)
#     user = forms.CharField(max_length=100)
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     mobile = forms.IntegerField()
#     address = forms.CharField(max_length=100)

