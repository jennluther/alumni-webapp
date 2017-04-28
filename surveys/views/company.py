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
### Edit Company
@view_function
def process_request(request):
    try:
        if request.urlparams[1] == 'internship':
            company = umod.Internship.objects.get(id=request.urlparams[0])
        elif request.urlparams[1] == 'offer':
            company = umod.Offers.objects.get(id=request.urlparams[0])
        else:
            company = umod.FullTime.objects.get(id=request.urlparams[0])
    except umod.FullTime.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    #process the form
    form = EditCompanyForm(request, initial={
        'company': company.company.name,
    })

    if form.is_valid():
        print('>>> form is valid')
        form.commit(company)
        if request.urlparams[1] == 'internship':
            return HttpResponseRedirect('/users/internship/' + str( company.id ))
        elif request.urlparams[1] == 'offer':
            return HttpResponseRedirect('/users/offer/' + str( company.id ))
        return HttpResponseRedirect('/users/currentjob/' + str( company.id ))

    #render the template
    context = {
        'company': company,
        'form': form,

    }
    return dmp_render(request, 'company.html', context)

class EditCompanyForm(FormMixIn, forms.Form):

    def init(self, user):
        self.fields['company'] = forms.ModelChoiceField(label='Company', queryset=umod.Company.objects.order_by('name').all())


    def commit(self, company):
        company.company = self.cleaned_data.get('company')
        company.save()


###########################
### Create Company if you already have a FullTime job record
@view_function
def create(request):
    try:
        current_job = umod.FullTime.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.FullTime.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    user = umod.User.objects.get(id=current_job.user.id)

    #process the form
    form = CreateCompanyForm(request)

    if form.is_valid():
        print('>>> form is valid')
        form.commit(current_job)
        return HttpResponseRedirect('/users/currentjob/' + str(current_job.id))

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

    def clean(self):
        try:
            umod.Company.objects.get(name=self.cleaned_data['name'], city=self.cleaned_data['city'], state=self.cleaned_data['state'] )
            raise forms.ValidationError("This Company already exists!")
        except umod.Company.DoesNotExist:
          #because we didn't get a match
          pass

        return self.cleaned_data

    def commit(self, current_job):
        company = umod.Company()
        company.name = self.cleaned_data.get('name')
        company.city = self.cleaned_data.get('city')
        company.state = self.cleaned_data.get('state')
        company.save()
        current_job.company = company
        current_job.save()


###########################
### Create Company for a new FullTime record
@view_function
def create_new(request):
    try:
        user = umod.User.objects.get(id=request.urlparams[0])
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')


    #process the form
    form = CreateCompanyForm(request)

    if form.is_valid():
        print('>>> form is valid')
        form.commit()
        company = umod.Company.objects.get(name=request.POST["name"], city=request.POST["city"], state=request.POST["state"])
        if request.urlparams[1] == 'internship':
            return HttpResponseRedirect('/users/internship.create/' + str(user.id) + '/' + str(company.id))
        if request.urlparams[1] == 'offer':
            return HttpResponseRedirect('/users/offer.create/' + str(user.id) + '/' + str(company.id))
        return HttpResponseRedirect('/users/currentjob.create/' + str(user.id) + '/' + str(company.id))

    #render the template
    context = {
        'form': form,
        'user': user,
    }
    return dmp_render(request, 'company.create_new.html', context)

class CreateCompanyForm(FormMixIn, forms.Form):

    def init(self):
        self.fields['name'] = forms.CharField(label='Company Name', max_length=100)
        self.fields['city'] = forms.CharField(label='City', max_length=30)
        self.fields['state'] = forms.ChoiceField(label='State', choices=umod.STATE)

    def clean(self):
        try:
            umod.Company.objects.get(name=self.cleaned_data['name'], city=self.cleaned_data['city'], state=self.cleaned_data['state'] )
            raise forms.ValidationError("This Company already exists!")
        except umod.Company.DoesNotExist:
          #because we didn't get a match
          pass

        return self.cleaned_data

    def commit(self):
        company = umod.Company()
        company.name = self.cleaned_data.get('name')
        company.city = self.cleaned_data.get('city')
        company.state = self.cleaned_data.get('state')
        company.save()
        return company



########################
###  Deleting Company
########### I don't think we want this to be an option.
