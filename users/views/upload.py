from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from django import forms
from formlib.form import FormMixIn
from users import alumni_import
from django.contrib.auth.decorators import permission_required
import io
import csv

@view_function
#####Only want admins to be able to upload alumni information
@permission_required('users.delete_user', login_url='/users/login/')
def process_request(request):

    form = FileFieldForm(request)

    if form.is_valid():
        uploaded_csv = io.TextIOWrapper(request.FILES['file_field'].file, encoding="ASCII")
        alumni_import.ImportAlumni(uploaded_csv)
        return HttpResponseRedirect('/users/users/all')



    #render the template
    context = {
        'form': form,
    }

    return dmp_render(request, 'upload.html', context)


class FileFieldForm(FormMixIn, forms.Form):
    form_enctype = 'multipart/form-data'
    form_submit = 'Upload'
    def init(self):
        self.fields['file_field'] = forms.FileField(label="Upload Alumni Information", required=False)
