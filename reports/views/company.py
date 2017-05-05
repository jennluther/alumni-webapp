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
def process_request(request):

    try:
        company = umod.Company.objects.get(id=request.urlparams[0])
    except umod.Company.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    alumni = umod.FullTime.objects.filter(company=request.urlparams[0])


    context = {
        'company': company,
        'alumni': alumni,
    }
    return dmp_render(request, 'company.html', context)
