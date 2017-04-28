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
        offer = umod.Offers.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.Offers.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    user = umod.User.objects.get(id=offer.user.id)
    ####I need to query to get the the current job!!!!

    #process the form
    form = EditOfferForm(request, initial={
        'intern_offer': offer.intern_offer,
    })

    if form.is_valid():
        form.commit(offer)
        return HttpResponseRedirect('/users/aluminfo/'+ str(user.id))

    #render the template
    context = {
        'form': form,
        'offer': offer,
    }

    return dmp_render(request, 'offer.html', context)

class EditOfferForm(FormMixIn, forms.Form):

    def init(self, user):
        self.fields['intern_offer'] = forms.BooleanField(label='Offer', required=False)

    def commit(self, offer):
        offer.intern_offer = self.cleaned_data.get('intern_offer')
        offer.save()



@view_function
def create(request):
    try:
        user = umod.User.objects.get(id=request.urlparams[0])
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    company = umod.Company.objects.get(id=request.urlparams[1])
    #process the form
    form = CreateOfferForm(request)


    if form.is_valid():
        print('>>> form is valid')
        form.commit(user, company)
        return HttpResponseRedirect('/users/aluminfo/' + str(user.id))

    #render the template
    context = {
        'form': form,
        'company': company,
    }
    return dmp_render(request, 'offer.create.html', context)

class CreateOfferForm(FormMixIn, forms.Form):

    def init(self, user):
        self.fields['intern_offer'] = forms.BooleanField(label='Offer', required=False)

    def commit(self,user, company):
        offer = umod.Offers()
        offer.user = user
        offer.company = company
        offer.intern_offer = self.cleaned_data.get('intern_offer')
        offer.save()



########################
###  Deleting offer

@view_function
def delete(request):
    try:
        offer = umod.Offers.objects.get(id=request.urlparams[0])
    except umod.Offers.DoesNotExist:
        return HttpResponseRedirect('/users/aluminfo/'+ str(offer.user.id))

    offer.delete()
    return HttpResponseRedirect('/users/aluminfo/'+ str(offer.user.id))
