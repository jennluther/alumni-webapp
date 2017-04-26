from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from django import forms
from formlib.form import FormMixIn

@view_function
def process_request(request):
    #pull all products from the DB
    try:
        internship = umod.Internship.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.Internship.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    user = umod.User.objects.get(id=internship.user.id)
    ####I need to query to get the the current job!!!!

    #process the form
    form = EditInternshipForm(request, initial={
        'position': internship.position_title,
        'how_obtained': internship.how_obtained,
        'hours_looking': internship.hours_looking,
    })

    if form.is_valid():
        form.commit(internship)
        return HttpResponseRedirect('/users/aluminfo/'+ str(user.id))

    #render the template
    context = {
        'form': form,
        'internship': internship,
    }

    return dmp_render(request, 'internship.html', context)

class EditInternshipForm(FormMixIn, forms.Form):

    def init(self, user):
        self.fields['position'] = forms.CharField(label='Position', max_length=30)
        self.fields['how_obtained'] = forms.CharField(label="How did you obtain this internship?", max_length=250)
        self.fields['hours_looking'] = forms.IntegerField(label='How many hours did you spend looking for this internship?')


    def commit(self, internship):
        internship.position_title = self.cleaned_data.get('position')
        internship.how_obtained = self.cleaned_data.get('how_obtained')
        internship.hours_looking = self.cleaned_data.get('hours_looking')
        internship.save()



@view_function
def create(request):
    try:
        user = umod.User.objects.get(id=request.urlparams[0])
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    company = umod.Company.objects.get(id=request.urlparams[1])
    #process the form
    form = CreateInternshipForm(request)


    if form.is_valid():
        print('>>> form is valid')
        form.commit(user, company)
        return HttpResponseRedirect('/users/aluminfo/' + str(user.id))

    #render the template
    context = {
        'form': form,
        'company': company,
    }
    return dmp_render(request, 'internship.create.html', context)

class CreateInternshipForm(FormMixIn, forms.Form):

    def init(self, user):
        self.fields['position'] = forms.CharField(label='Position', max_length=30)
        self.fields['how_obtained'] = forms.CharField(label="How did you obtain this internship?", max_length=250)
        self.fields['hours_looking'] = forms.IntegerField(label='How many hours did you spend looking for this internship?')


    def commit(self,user, company):
        internship = umod.Internship()
        internship.position_title = self.cleaned_data.get('position')
        internship.how_obtained = self.cleaned_data.get('how_obtained')
        internship.hours_looking = self.cleaned_data.get('hours_looking')
        internship.company = company
        internship.user = user
        internship.save()
