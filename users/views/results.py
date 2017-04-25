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
    #
    try:
        exit_survey = umod.ExitSurvey.objects.get(user=request.urlparams[0])
    except umod.ExitSurvey.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    user = umod.User.objects.get(id=request.urlparams[0])


    #render the template
    context = {
        'exit_survey': exit_survey,
        'user': user,
    }

    return dmp_render(request, 'results.html', context)
