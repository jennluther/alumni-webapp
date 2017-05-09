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
@permission_required('users.delete_user', login_url='/users/login/')
def process_request(request):

    alumni = umod.FullTime.objects.filter(company=request.urlparams[0])
    company = umod.Company.objects.get(id=request.urlparams[0])

    response = HttpResponse(content_type='application/ms-excel')

    if request.urlparams[1] == 'current':
        alumni = alumni.filter(current_job=True)
        response['Content-Disposition'] = 'attachment; filename="' + company.name + '-Current-Alumni.xls"'
    elif request.urlparams[1] == "past":
        alumni = alumni.filter(current_job=False)
        response['Content-Disposition'] = 'attachment; filename="' + company.name + '-Past-Alumni.xls"'
    else:
        alumni = alumni.order_by('user__last_name').all()
        response['Content-Disposition'] = 'attachment; filename="' + company.name + '-Alumni.xls"'

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

    rows = alumni.all().values_list('user__first_name','user__last_name', 'user__email', 'user__street', 'user__city', 'user__state', 'user__zipcode', 'user__country', 'user__phone', 'user__graduation_year', 'user__graduation_semester', 'user__program')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
