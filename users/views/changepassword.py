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
        user = umod.User.objects.get(id=request.user.id)
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    #process the form
    form = ChangePasswordForm(request, initial={
        'username': user.username,
        'password': user.password,
    })
    if form.is_valid():
        print('>>> form is valid')
        form.commit(user)
        return HttpResponseRedirect('/users/account/')

    #render the template
    context = {
        'form': form,
    }

    return dmp_render(request, 'changepassword.html', context)

class ChangePasswordForm(FormMixIn, forms.Form):

    def init(self):
        self.fields['username'] = forms.CharField(widget=forms.HiddenInput(), required=False)
        self.fields['password'] = forms.CharField(label='Password', widget=forms.PasswordInput)
        self.fields['new_password1'] = forms.CharField(label="New Password", widget=forms.PasswordInput)
        self.fields['new_password2'] = forms.CharField(label="Confirm Password", widget=forms.PasswordInput,
            help_text='Enter the same password as above')

    def clean(self):
        password = self.cleaned_data.get('password')
        self.user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('User does not exist.  Try again.')
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 != new_password2:
            raise forms.ValidationError('Passwords do not match')

    def commit(self, user):
        user.set_password(self.cleaned_data.get('new_password1'))
        user.save()
