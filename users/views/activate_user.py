from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from django import forms
from formlib.form import FormMixIn

#################
### Change Password
@view_function
def process_request(request):
    #pull all products from the DB
    try:
        person = umod.User.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    #process the form
    form = ChangePasswordForm(request, initial={
        'username': person.username,
    })
    if form.is_valid():
        print('>>> form is valid')
        form.commit(person)
        return HttpResponseRedirect('/users/aluminfo/' + str(person.id) + '/')

    #render the template
    context = {
        'form': form,
        'person': person,
    }

    return dmp_render(request, 'activate_user.html', context)

class ChangePasswordForm(FormMixIn, forms.Form):

    def init(self):
        self.fields['username'] = forms.CharField(widget=forms.HiddenInput(), required=False)
        self.fields['new_password1'] = forms.CharField(label="New Password", widget=forms.PasswordInput)
        self.fields['new_password2'] = forms.CharField(label="Confirm Password", widget=forms.PasswordInput,
            help_text='Enter the same password as above')

    def clean(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 != new_password2:
            raise forms.ValidationError('Passwords do not match')

    def commit(self, person):
        person.set_password(self.cleaned_data.get('new_password1'))
        person.save()
