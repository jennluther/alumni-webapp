from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django import forms
from .. import dmp_render, dmp_render_to_string
from users.models import Person


@view_function
def process_request(request):

  #process the form
  form = SignupForm()
  if request.method == 'POST': # just submitted the form
    form = SignupForm(request.POST)
    if form.is_valid():
        # create a user object
        # fill user object with the data from the form
        p = Person()
        p.first_name = form.cleaned_data.get('first_name')
        p.last_name = form.cleaned_data.get('last_name')
        p.email = form.cleaned_data.get('email')
        p.username = form.cleaned_data.get('username')
        p.set_password(form.cleaned_data.get('password'))
        p.save() # this is our insert statement right here
        return HttpResponseRedirect('/homepage/index/')


  template_vars = {
    'form': form,
  }

  return dmp_render(request, 'signup.html', template_vars)

class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True, max_length=100)
    last_name = forms.CharField(label='Last Name', required=True, max_length=100)
    email = forms.
    username = forms.CharField(label='Username', required=True, max_length=100)
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Re-enter your Password', required=True, max_length=100, widget=forms.PasswordInput())


    def clean_username(self):
        username = self.cleaned_data.get('username')
        # if not username.lower().strip().startswith('a'):
        #     raise forms.ValidationError('Please start your username with the letter "a".')
        # check the availability of the username(method #1)
        # try:
        #     user = User.objects.get(username=self.cleaned_data.get('username')) #shouldn't it be username == etc.?
        #     raise forms.ValidationError('This username has already been taken. Please enter a new username.')
        # except User.DoesNotExist:
        #     pass #this is what we hope happens, it means the username is ok!

        # check the availability of the username (method #2)
        users = User.objects.filter(username=self.cleaned_data.get('username'))
        if len(users) > 0:
            raise forms.ValidationError('This username has already been used. Please enter a new username.')
        return username

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords need to match. Please try again.')
        return self.cleaned_data
