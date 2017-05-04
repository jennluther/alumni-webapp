from django.contrib.auth import logout
from django_mako_plus import view_function
from .. import dmp_render, dmp_render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect

@view_function
def process_request(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/homepage/index')
