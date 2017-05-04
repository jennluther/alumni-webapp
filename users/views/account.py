from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from django import forms
from formlib.form import FormMixIn
from django.contrib.auth.decorators import permission_required

#################
### Edit MyAccount
@view_function
@permission_required('users.change_user', login_url='/users/login/')
def process_request(request):
    #pull all products from the DB
    try:
        user = umod.User.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    #process the form
    form = MyAccountForm(request, initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'city': user.city,
        'state': user.state,
    })
    if form.is_valid():
        print('>>> form is valid')
        form.commit(user)
        return HttpResponseRedirect('/users/account/')

    #render the template
    context = {
        'user': user,
        'form': form,

    }
    return dmp_render(request, 'account.html', context)

class MyAccountForm(FormMixIn, forms.Form):

    def init(self):
        self.fields['first_name'] = forms.CharField(label='First Name', max_length=100)
        self.fields['last_name'] = forms.CharField(label='Last Name', max_length=100)
        self.fields['username'] = forms.CharField(label='User Name', max_length=100)
        self.fields['email'] = forms.EmailField(label='Email')
        self.fields['phone'] = forms.CharField(label='Phone', max_length=30)
        self.fields['city'] = forms.CharField(label='City', max_length=30)
        self.fields['state'] = forms.CharField(label='State')

    def clean_username(self):
       username = self.cleaned_data.get('username')
       if umod.User.objects.filter(username=username).exclude(id=self.request.user.id):
           raise forms.ValidationError('Username is already in use.')
       return username

    def commit(self, user):
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone')
        company.name = self.cleaned_data.get('street_address')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')

        user.save()
