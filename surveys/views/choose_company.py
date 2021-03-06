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
### Choose Company
@view_function
@permission_required('users.add_exitsurvey', login_url='/users/login/')
def process_request(request):
    try:
        alumni = umod.User.objects.get(id=request.urlparams[0])
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    form = ChooseCompanyForm(request)

    if request.urlparams[1] == 'internship':
        newcompany_link = "/surveys/company.create_new/" + str(alumni.id) + "/internship"
    elif request.urlparams[1] == 'offer':
        newcompany_link = "/surveys/company.create_new/" + str(alumni.id) + "/offer"
    else:
        newcompany_link = "/surveys/company.create_new/" + str(alumni.id) + "/"

    if form.is_valid():
        form.commit()
        if request.urlparams[1] == 'internship':
            return HttpResponseRedirect('/users/internship.create/' + str(alumni.id) + '/' + str(request.POST['company']))
        elif request.urlparams[1] == 'offer':
            return HttpResponseRedirect('/users/offer.create/' + str(alumni.id) + '/' + str(request.POST['company']))
        return HttpResponseRedirect('/users/currentjob.create/' + str(alumni.id) + '/' + str(request.POST['company']))

    context = {
        'form': form,
        'alumni': alumni,
        'newcompany_link': newcompany_link
    }
    return dmp_render(request, 'choose_company.html', context)


class ChooseCompanyForm(FormMixIn, forms.Form):

    def init(self):
        self.fields['company'] = forms.ModelChoiceField(label='Company', queryset=umod.Company.objects.order_by('name').all())


    def commit(self):
        company = self.cleaned_data.get('company')
        return company
