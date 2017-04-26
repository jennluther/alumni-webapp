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


####################
@view_function
def process_request(request):
    #pull all products from the DB
    try:
        user = umod.User.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    try:
        exitSurvey = umod.ExitSurvey.objects.get(user = user.id)
    except umod.ExitSurvey.DoesNotExist:
        exitSurvey = False

    try:
        pastFullTime = umod.FullTime.objects.filter(user = user.id, current_job = False)
        if not pastFullTime:
            pastFullTime = False
        print(pastFullTime)
    except umod.FullTime.DoesNotExist:
        pastFullTime = False

    try:
        currentFullTime = umod.FullTime.objects.get(user = user.id, current_job = True)
    except umod.FullTime.DoesNotExist:
        currentFullTime = False

    try:
        internship = umod.Internship.objects.filter(user = user.id)
        if not internship:
            internship = False
    except umod.Internship.DoesNotExist:
        internship = False






    #render the template
    context = {
        'user': user,
        'exitSurvey': exitSurvey,
        'pastFullTime': pastFullTime,
        'currentFullTime': currentFullTime,
        'internship': internship,
    }
    return dmp_render(request, 'aluminfo.html', context)
