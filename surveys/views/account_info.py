from django import forms
from django.conf import settings
from users import models as umod
from django.forms import widgets

# add to your views
def account_info(request):
    form = ContactForm

    return render(request, 'contact.html', {
        'form': form_class,
    })


class AccountInfo(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    #make company a drop down list with the company names
    company = forms.CharField(required=False)
    salary = forms.DecimalField(required=False)
