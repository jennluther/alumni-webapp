from django.contrib.auth import authenticate, login
from django_mako_plus import view_function
from .. import dmp_render, dmp_render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
from users import models as umod
from django import forms
from formlib.form import FormMixIn

@view_function
def process_request(request):

    form = LoginForm(request)
    if form.is_valid():
        #log the user in
        login(request, form.user)
        form.commit()
        #redirect to the myaccount page
        return HttpResponseRedirect("/homepage/index/")

    #if not authenticated
    return dmp_render(request, 'login.html',{
        'form': form,
    })


class LoginForm(FormMixIn, forms.Form):

    def init(self):
        self.form_action = "/account/login.modal/"
        self.fields['username'] = forms.CharField(required=True)
        self.fields['password'] = forms.CharField(required=True, widget=forms.PasswordInput())

    def clean(self):
        '''Authenticates the username and password'''
        #authenticates the user
        self.user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid username or password')
        if self.user.is_authenticated():
            print(">>>>>is authenticated")


###################
@view_function
def modal(request):

    form = LoginForm(request)
    if form.is_valid():
        #log the user in
        login(request, form.user)
        form.commit()
        #redirect to the myaccount page
        return HttpResponse('<script>window.location.href ="/homepage/index/";</script>')

    #if not authenticated
    return dmp_render(request, 'login.modal.html',{
        'form': form,
    })
