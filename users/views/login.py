from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django import forms
from .. import dmp_render, dmp_render_to_string
from users.models import Person


@view_function
def process_request(request):

  #if already logged in, go to the account area
  # if request.user.is_authenticated():
  #     return HttpResponseRedirect('/account/login/')

  #process the form
  form = LoginForm()
  if request.method == 'POST': # just submitted the form
    form = LoginForm(request.POST)
    if form.is_valid():
        # log the user in - connect the user to the request
        person = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        login(request, person)
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

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))


    def clean(self):
        person = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if person == None:
            raise forms.ValidationError('The username and password pair was not found in our system.')
        return self.cleaned_data
