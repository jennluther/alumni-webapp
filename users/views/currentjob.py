from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from django import forms
from formlib.form import FormMixIn
from django.contrib.auth.decorators import permission_required

@view_function
@permission_required('users.change_fulltime', login_url='/users/login/')
def process_request(request):
    #pull all products from the DB
    try:
        current_job = umod.FullTime.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.FullTime.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    alumni = umod.User.objects.get(id=current_job.user.id)
    ####I need to query to get the the current job!!!!

    #process the form
    form = EditCurrentJobForm(request, initial={
        'position': current_job.position_title,
        'position_description': current_job.position_description,
        'current_job': current_job.current_job,
        'date_accepted': current_job.date_accepted,
        'start_date': current_job.start_date,
        'end_date': current_job.end_date,
        'salary': current_job.salary,
        'avg_hours_week': current_job.avg_hours_week,
        'satisfaction': current_job.satisfaction,
        'projected_raise_time_months': current_job.projected_raise_time_months,
        'family_friendly': current_job.family_friendly,
        'family_friendly_response': current_job.family_friendly_response,
        'pros': current_job.pros,
        'cons': current_job.cons,
        'contact': current_job.contact,
        'ft_hours_looking': current_job.ft_hours_looking,
    })

    form.object = current_job.company

    if form.is_valid():
        print('>>> form is valid')
        form.commit(current_job)
        return HttpResponseRedirect('/users/aluminfo/'+ str(alumni.id))

    #render the template
    context = {
        'form': form,
        'current_job': current_job,
    }

    return dmp_render(request, 'currentjob.html', context)

class EditCurrentJobForm(FormMixIn, forms.Form):

    def init(self, alumni):
        self.fields['position'] = forms.CharField(label='Position', max_length=30)
        self.fields['position_description'] = forms.ChoiceField(choices=umod.POSITION_CHOICES, label='Position Description')
        self.fields['current_job'] = forms.BooleanField(label='Current Job', required=False)
        self.fields['skills'] = forms.MultipleChoiceField(choices=umod.SKILLS_CHOICES, label='Skills', required=False)
        self.fields['date_accepted'] = forms.DateField(label='Date of job offer acceptance')
        self.fields['start_date'] = forms.DateField(label='Start Date')
        self.fields['end_date'] = forms.DateField(label='End Date', required=False)
        self.fields['salary'] = forms.DecimalField(label='Salary', max_digits=15)
        self.fields['avg_hours_week'] = forms.IntegerField(label='Averages hours/week')
        self.fields['satisfaction'] = forms.ChoiceField(choices=umod.SATISFACTION_CHOICES, label='Satisfaction')
        self.fields['projected_raise_time_months'] = forms.IntegerField(label='Projected Raise Time (months)')
        self.fields['family_friendly'] = forms.BooleanField(label='Is this company family friendly?', required=False)
        self.fields['family_friendly_response'] = forms.CharField(label='Why', max_length=200)
        self.fields['pros'] = forms.CharField(label='Pros', max_length=200)
        self.fields['cons'] = forms.CharField(label='Cons', max_length=200)
        self.fields['contact'] = forms.ChoiceField(label='Would you be willing to act as a contact for this company?', choices=umod.CONTACT_CHOICES)
        self.fields['ft_hours_looking'] = forms.IntegerField(label='How many hours did you spend looking for this job?')

    def commit(self, current_job):
        current_job.position_title = self.cleaned_data.get('position')
        current_job.position_description = self.cleaned_data.get('position_description')
        current_job.current_job = self.cleaned_data.get('current_job')
        skills = self.cleaned_data.get('skills')
        for s in skills:
            if umod.Skills.objects.get(skill=s, full_time=current_job):
                pass
            else:
                job_skills = umod.Skills()
                job_skills.full_time = current_job
                job_skills.skill = s
                job_skills.save()
                print( ">>>>>>>>>", job_skills.skill)
        current_job.date_accepted = self.cleaned_data.get('date_accepted')
        current_job.start_date = self.cleaned_data.get('start_date')
        current_job.end_date = self.cleaned_data.get('end_date')
        current_job.salary = self.cleaned_data.get('salary')
        current_job.avg_hours_week = self.cleaned_data.get('avg_hours_week')
        current_job.satisfaction = self.cleaned_data.get('satisfaction')
        current_job.projected_raise_time_months = self.cleaned_data.get('projected_raise_time_months')
        current_job.family_friendly = self.cleaned_data.get('family_friendly')
        current_job.family_friendly_response = self.cleaned_data.get('family_friendly_response')
        current_job.pros = self.cleaned_data.get('pros')
        current_job.cons = self.cleaned_data.get('cons')
        current_job.contact = self.cleaned_data.get('contact')
        current_job.ft_hours_looking = self.cleaned_data.get('ft_hours_looking')
        current_job.save()



@view_function
@permission_required('users.add_fulltime', login_url='/users/login/')
def create(request):
    try:
        alumni = umod.User.objects.get(id=request.urlparams[0])
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    company = umod.Company.objects.get(id=request.urlparams[1])
    #process the form
    form = CreateJobForm(request)


    if form.is_valid():
        print('>>> form is valid')
        form.commit(alumni, company)
        return HttpResponseRedirect('/users/aluminfo/' + str(alumni.id))

    #render the template
    context = {
        'form': form,
        'company': company,
    }
    return dmp_render(request, 'currentjob.create.html', context)

class CreateJobForm(FormMixIn, forms.Form):

    def init(self, alumni):
        self.fields['position'] = forms.CharField(label='Position', max_length=30)
        self.fields['position_description'] = forms.ChoiceField(choices=umod.POSITION_CHOICES, label='Position Description')
        self.fields['date_accepted'] = forms.DateField(label='Date of job offer acceptance')
        self.fields['start_date'] = forms.DateField(label='Start Date')
        self.fields['end_date'] = forms.DateField(label='End Date', required=False)
        self.fields['salary'] = forms.DecimalField(label='Salary', max_digits=15)
        self.fields['avg_hours_week'] = forms.IntegerField(label='Averages hours/week')
        self.fields['satisfaction'] = forms.ChoiceField(choices=umod.SATISFACTION_CHOICES, label='Satisfaction')
        self.fields['projected_raise_time_months'] = forms.IntegerField(label='Projected Raise Time (months)')
        self.fields['family_friendly'] = forms.BooleanField(label='Is this company family friendly?', required=False)
        self.fields['family_friendly_response'] = forms.CharField(label='Why', max_length=200)
        self.fields['pros'] = forms.CharField(label='Pros', max_length=200)
        self.fields['cons'] = forms.CharField(label='Cons', max_length=200)
        self.fields['contact'] = forms.ChoiceField(label='Would you be willing to act as a contact for this company?', choices=umod.CONTACT_CHOICES)
        self.fields['ft_hours_looking'] = forms.IntegerField(label='How many hours did you spend looking for this job?')


    def commit(self,alumni, company):
        job = umod.FullTime()
        job.position_title = self.cleaned_data.get('position')
        job.position_description = self.cleaned_data.get('position_description')
        job.date_accepted = self.cleaned_data.get('date_accepted')
        job.start_date = self.cleaned_data.get('start_date')
        job.end_date = self.cleaned_data.get('end_date')
        job.salary = self.cleaned_data.get('salary')
        job.avg_hours_week = self.cleaned_data.get('avg_hours_week')
        job.satisfaction = self.cleaned_data.get('satisfaction')
        job.projected_raise_time_months = self.cleaned_data.get('projected_raise_time_months')
        job.family_friendly = self.cleaned_data.get('family_friendly')
        job.family_friendly_response = self.cleaned_data.get('family_friendly_response')
        job.pros = self.cleaned_data.get('pros')
        job.cons = self.cleaned_data.get('cons')
        job.contact = self.cleaned_data.get('contact')
        job.ft_hours_looking = self.cleaned_data.get('ft_hours_looking')
        job.company = company
        job.user = alumni

        job.save()

########################
###  Deleting currentjob

@view_function
@permission_required('users.delete_fulltime', login_url='/users/login/')
def delete(request):
    try:
        current_job = umod.FullTime.objects.get(id=request.urlparams[0])
    except umod.FullTime.DoesNotExist:
        return HttpResponseRedirect('/users/aluminfo/'+ str(current_job.user.id))

    current_job.delete()
    return HttpResponseRedirect('/users/aluminfo/'+ str(current_job.user.id))
