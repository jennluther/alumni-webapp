from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponseRedirect

##import models
from surveys.models import *

@view_function
#@login_required(login_url='/homepage/login')
def process_request(request):
    context = {
        'now': datetime.now(),
    }
    return dmp_render(request, 'index.html', context)
