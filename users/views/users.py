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


@view_function
def process_request(request):
    #pull all users from the DB
    exitsurvey = []
    for e in umod.ExitSurvey.objects.all():
        exitsurvey.append(e.user.id)
        print("$$$$$$", e.user.id)

    users = umod.User.objects.filter(alumni=True)

    if request.urlparams[0] == 'completed':
        users = users.filter(id__in=exitsurvey)
    elif request.urlparams[0] == "incomplete":
        users = users.exclude(id__in=exitsurvey)
    elif request.urlparams[0] == "MISM":
        users = users.filter(program__icontains='MISM')
    elif request.urlparams[0] == "BSIS":
        users = users.filter(program__icontains='BSIS')
    else:
        users = users.order_by('last_name').all()

    form = SearchForm(request)
    if form.is_valid():
        form.commit()
        users = umod.User.objects.filter(Q(first_name__icontains=form.cleaned_data.get('search')) | Q(last_name__icontains=form.cleaned_data.get('search')))







    #render the template
    context = {
        'users': users,
        'form' : form,

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
