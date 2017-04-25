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
        company = umod.FullTime.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.Company.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    #process the form
    form = EditCompanyForm(request, initial={
        'name': company.company.name,
        'city': company.company.city,
        'state': company.company.state,
    })

    if form.is_valid():
        print('>>> form is valid')
        form.commit(company)
        return HttpResponseRedirect('/users/currentjob/' + company.id )

    #render the template
    context = {
        'company': company,
        'form': form,

    }
    return dmp_render(request, 'company.html', context)

class EditCompanyForm(FormMixIn, forms.Form):

    def init(self, user):
        self.fields['name'] = forms.CharField(label='Company Name', max_length=100)
        self.fields['city'] = forms.CharField(label='City', max_length=100)
        self.fields['state'] = forms.ChoiceField(label='State', choices=umod.STATE)



    def commit(self, company):
        company.company.name = self.cleaned_data.get('name')
        company.company.city = self.cleaned_data.get('city')
        company.company.state = self.cleaned_data.get('state')
        company.save()


###########################
### Create Company
@view_function
def create(request):

    #process the form
    form = CreateCompanyForm(request)

    if form.is_valid():
        print('>>> form is valid')
        form.commit()
        return HttpResponseRedirect('/users/fulltime/')

    #render the template
    context = {
        'form': form,
    }
    return dmp_render(request, 'company.create.html', context)

class CreateCompanyForm(FormMixIn, forms.Form):

    def init(self):
        self.fields['name'] = forms.CharField(label='Company Name', max_length=100)
        self.fields['city'] = forms.CharField(label='City', max_length=30)
        self.fields['state'] = forms.ChoiceField(label='State', choices=umod.STATE)


    def commit(self):
        company = umod.Company()
        company.name = self.cleaned_data.get('name')
        company.city = self.cleaned_data.get('city')
        company.state = self.cleaned_data.get('state')
        company.save()




########################
###  Deleting Company
########### I don't think we want this to be an option.
