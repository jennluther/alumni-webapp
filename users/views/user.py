from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from django import forms
from formlib.form import FormMixIn
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.decorators import permission_required


#################
### Edit User
@view_function
def process_request(request):
    #pull all products from the DB
    try:
        user1 = umod.User.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    #process the form
    form = EditUserForm(request, initial={
        'first_name': user1.first_name,
        'last_name': user1.last_name,
        'username': user1.username,
        'password': user1.password,
        'graduation_semester': user1.graduation_semester,
        'graduation_year' : user1.graduation_year,
        'street' : user1.street,
        'city': user1.city,
        'state': user1.state,
        'country': user1.country,
        'zipcode' : user1.zipcode,
        'phone': user1.phone,
        'email': user1.email,
        'program' : user1.program,
        #is there a way to go through all of their internships and output them
    })
    if form.is_valid():
        print('>>> form is valid')
        form.commit(user1)
        return HttpResponseRedirect('/users/users/')

    #render the template
    context = {
        'user1': user1,
        'form': form,

    }
    return dmp_render(request, 'user.html', context)

class EditUserForm(FormMixIn, forms.Form):

    def init(self, user):
        self.fields['first_name'] = forms.CharField(label='First Name', max_length=100)
        self.fields['last_name'] = forms.CharField(label='Last Name', max_length=100)
        self.fields['username'] = forms.CharField(label="Username", max_length=100)
        self.fields['password'] = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
        self.fields['email'] = forms.EmailField(label='Email', required=False)
        self.fields['graduation_semester'] = forms.ChoiceField(choices=umod.SEMESTER_CHOICES, label='Graduation Semester', required=False)
        self.fields['graduation_year'] = forms.IntegerField(label='Graduation Year')
        self.fields['street'] = forms.CharField(label='Street', required=False)
        self.fields['city'] = forms.CharField(label='City', max_length=30, required=False)
        self.fields['state'] = forms.CharField(label='State', required=False)
        self.fields['country'] = forms.CharField(label='Country', required=False)
        self.fields['zipcode'] = forms.IntegerField(label='Zip Code', required=False)
        self.fields['phone'] = forms.CharField(label='Phone', required=False)
        self.fields['program'] = forms.ChoiceField(choices=umod.PROGRAM_CHOICES, label='Program')




    def commit(self, user1):
        user1.first_name = self.cleaned_data.get('first_name')
        user1.last_name = self.cleaned_data.get('last_name')
        user1.username = self.cleaned_data.get('username')
        user1.set_password(self.cleaned_data.get('password'))
        user1.street = self.cleaned_data.get('street')
        user1.city = self.cleaned_data.get('city')
        user1.state = self.cleaned_data.get('state')
        user1.country = self.cleaned_data.get('country')
        user1.zipcode = self.cleaned_data.get('zipcode')
        user1.phone = self.cleaned_data.get('phone')
        user1.email = self.cleaned_data.get('email')
        user1.graduation_year = self.cleaned_data.get('graduation_year')
        user1.graduation_semester = self.cleaned_data.get('graduation_semester')
        user1.program = self.cleaned_data.get('program')
        user1.save()


###########################
### Create User
@view_function
def create(request):

    #process the form
    form = CreateUserForm(request)

    if form.is_valid():
        print('>>> form is valid')
        form.commit()
        return HttpResponseRedirect('/users/users/')

    #render the template
    context = {
        'form': form,
    }
    return dmp_render(request, 'user.create.html', context)

class CreateUserForm(FormMixIn, forms.Form):

    def init(self):
        self.fields['first_name'] = forms.CharField(label='First Name', max_length=100)
        self.fields['last_name'] = forms.CharField(label='Last Name', max_length=100)
        self.fields['username'] = forms.CharField(label="Username", max_length=100)
        self.fields['password'] = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
        self.fields['email'] = forms.EmailField(label='Email')
        self.fields['graduation_semester'] = forms.ChoiceField(choices=umod.SEMESTER_CHOICES, label='Graduation Semester')
        self.fields['graduation_year'] = forms.IntegerField(label='Graduation Year')
        self.fields['street'] = forms.CharField(label='Street')
        self.fields['city'] = forms.CharField(label='City', max_length=30)
        self.fields['state'] = forms.CharField(label='State')
        self.fields['country'] = forms.CharField(label='Country')
        self.fields['zipcode'] = forms.IntegerField(label='Zip Code')
        self.fields['phone'] = forms.CharField(label='Phone')
        self.fields['program'] = forms.ChoiceField(choices=umod.PROGRAM_CHOICES, label='Program')



    def clean_username(self):
       username = self.cleaned_data.get('username')
       if umod.User.objects.filter(username=username).exclude(id=self.request.user.id):
           raise forms.ValidationError('Username is already in use.')
       return username

    def commit(self):
        user = umod.User()
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.username = self.cleaned_data.get('username')
        user.set_password(self.cleaned_data.get('password'))
        user.street = self.cleaned_data.get('street')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.country = self.cleaned_data.get('country')
        user.zipcode = self.cleaned_data.get('zipcode')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.graduation_year = self.cleaned_data.get('graduation_year')
        user.graduation_semester = self.cleaned_data.get('graduation_semester')
        user.program = self.cleaned_data.get('program')
        user.save()




########################
###  Deleting user

@view_function
def delete(request):
    try:
        user = umod.User.objects.get(id=request.urlparams[0])
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/users/users')

    user.delete()
    return HttpResponseRedirect('/users/users')
