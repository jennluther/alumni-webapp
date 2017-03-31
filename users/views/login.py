from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django import forms
from .. import dmp_render, dmp_render_to_string
from users.models import User
from formlib.form import FormMixIn


@view_function
def process_request(request):
  #process the form
  form = LoginForm(request)

  if form.is_valid():
        # log the user in - connect the user to the request
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        login(request, user)
        #return HttpResponseRedirect('/homepage/index/')
        return HttpResponse('''
        <script>
            window.location.href = '/homepage/index/';
        </script>
        ''')


  template_vars = {
    'form': form,
  }

  return dmp_render(request, 'login.html', template_vars)

class LoginForm(FormMixIn, forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100)
    password = forms.CharField(label='Password', required=True, max_length=100)


    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError('The username and password pair was not found in our system.')
        return self.cleaned_data
