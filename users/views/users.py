from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from formlib.form import FormMixIn
from django import forms
import io
import xlsxwriter
from django.utils.translation import ugettext


@view_function
@permission_required('users.add_group', login_url='/users/login/')
def process_request(request):
    #pull all users from the DB
    exitsurvey = []
    for e in umod.ExitSurvey.objects.all():
        exitsurvey.append(e.user.id)
        print("$$$$$$", e.user.id)

    alumni = umod.User.objects.filter(alumni=True)

    if request.urlparams[0] == 'completed':
        alumni = alumni.filter(id__in=exitsurvey)
        export_link = '/users/export/completed'
    elif request.urlparams[0] == "incomplete":
        alumni = alumni.exclude(id__in=exitsurvey)
        export_link = '/users/export/incomplete'
    elif request.urlparams[0] == "MISM":
        alumni = alumni.filter(program__icontains='MISM')
        export_link = '/users/export/MISM'
    elif request.urlparams[0] == "BSIS":
        alumni = alumni.filter(program__icontains='BSIS')
        export_link = '/users/export/BSIS'
    else:
        alumni = alumni.order_by('last_name').all()
        export_link = '/users/export/'

    form = SearchForm(request)
    if form.is_valid():
        form.commit()
        alumni = umod.User.objects.filter(Q(first_name__icontains=form.cleaned_data.get('search')) | Q(last_name__icontains=form.cleaned_data.get('search')))






    #render the template
    context = {
        'alumni': alumni,
        'form' : form,
        'export_link': export_link,

    }
    return dmp_render(request, 'users.html', context)


class SearchForm(FormMixIn, forms.Form):
    form_submit = ""
    open_btn = ''
    close_btn = ''
    def init(self):
        self.fields['search'] = forms.CharField(label='Search', max_length=100)
    def commit(self):
        # if all checks out then do the work (search the database)
        search = self.cleaned_data.get('search')
