from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from django import forms
from formlib.form import FormMixIn
from users import alumni_import

@view_function
def process_request(request):

    form = FileFieldForm(request)

    if form.is_valid():
        print(">>>>>>>>POST", request.FILES)
        uploaded_csv = request.FILES['file_field'].read()
        print(">>>>>>>>>>", uploaded_csv)
        alumni_import.ImportAlumni(uploaded_csv)
        return HttpResponseRedirect('/users/users/')



    #render the template
    context = {
        'form': form,
    }

    return dmp_render(request, 'upload.html', context)


class FileFieldForm(FormMixIn, forms.Form):
    form_enctype = 'multipart/form-data'
    def init(self):
        self.fields['file_field'] = forms.FileField(label="Upload Alumni Information", required=False)
