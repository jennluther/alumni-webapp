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
import xlwt
from django.utils.translation import ugettext


@view_function
@permission_required('users.add_group', login_url='/users/login/')
def process_request(request):

    alumni = umod.User.objects.filter(alumni=True)

    exitsurvey = []
    for e in umod.ExitSurvey.objects.all():
        exitsurvey.append(e.user.id)

    response = HttpResponse(content_type='application/ms-excel')

    if request.urlparams[0] == 'completed':
        alumni = alumni.filter(id__in=exitsurvey)
        response['Content-Disposition'] = 'attachment; filename="completed-alumni.xls"'
    elif request.urlparams[0] == "incomplete":
        alumni = alumni.exclude(id__in=exitsurvey)
        response['Content-Disposition'] = 'attachment; filename="incomplete-alumni.xls"'
    elif request.urlparams[0] == "MISM":
        alumni = alumni.filter(program__icontains='MISM')
        response['Content-Disposition'] = 'attachment; filename="mism-alumni.xls"'
    elif request.urlparams[0] == "BSIS":
        alumni = alumni.filter(program__icontains='BSIS')
        response['Content-Disposition'] = 'attachment; filename="bsis-alumni.xls"'
    else:
        alumni = alumni.order_by('last_name').all()
        response['Content-Disposition'] = 'attachment; filename="alumni.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Alumni')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['First name', 'Last name', 'Email', 'Street', 'City', 'State', 'Zip', 'Country', 'Phone', 'Graduation Year', 'Graduation Semester', 'Program' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = alumni.all().values_list('first_name','last_name', 'email', 'street', 'city', 'state', 'zipcode', 'country', 'phone', 'graduation_year', 'graduation_semester', 'program')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
