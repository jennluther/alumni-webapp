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

    companies = umod.Company.objects.distinct('name')
    alumni_count = umod.FullTime.objects.distinct('company').count()

    context = {
        'companies': companies,
        'alumni_count': alumni_count
    }
    return dmp_render(request, 'companies.html', context)
