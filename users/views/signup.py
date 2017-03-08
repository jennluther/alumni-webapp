from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django import forms
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from users.models import *



@view_function
def process_request(request):

  #process the form
  form = SignupForm()
  if request.method == 'POST': # just submitted the form
    form = SignupForm(request.POST)
    if form.is_valid():
        # create a user object
        # fill user object with the data from the form
        # d = umod.Donation()
        u = umod.User()
        u.first_name = form.cleaned_data.get('first_name')
        u.last_name = form.cleaned_data.get('last_name')
        u.email = form.cleaned_data.get('email')
        u.username = form.cleaned_data.get('username')
        u.set_password(form.cleaned_data.get('password'))

        # d.give_back = form.cleaned_data.get('give_back')
        # d.my_choice = form.cleaned_data.get('my_choice')


        u.save() # this is our insert statement right here




        return HttpResponseRedirect('/homepage/index/')


  template_vars = {
    'form': form,
  }

  return dmp_render(request, 'signup.html', template_vars)

class SignupForm(forms.Form):

    GIVE_CHOICES = [
        ["Money", "Money (donations to department, scholarship funds, etc.)"],
        ["Time", "Time (mentorship, guest lectures, etc.)"],
        ["Both", "Both"],
        ["No", "I don't plan on giving back"],
    ]

    MY_CHOICE_CHOICES = [
        ["Y", "Yes"],
        ["N", "No"],
    ]

    first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    # give_back = forms.ChoiceField(label='When you can, will you give back to the IS program?', required=True, choices=GIVE_CHOICES)
    # my_choice = forms.ChoiceField(label="Did you participate in My Choice to Give?", required=True, choices=MY_CHOICE_CHOICES)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        print('<<<<<<<<<<<<<<<clean')

        #check the availability of the username (method #2)
        # this says, "Hey db, look at your person table, filter your list of users based on the username I just got. If the username isn't already in use, there should be no results of the filter."
        # So if the length of the list of filtered users is greater than 0, then that means there is already the same username stored in the db and the one inputted is a duplicate.
        users = User.objects.filter(username=self.cleaned_data.get('username'))
        if len(users) > 0:
            raise forms.ValidationError('This username has already been used. Please enter a new username.')
        return username
