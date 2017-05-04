from django import forms
from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect, HttpResponse
from .. import dmp_render, dmp_render_to_string
from django.forms import widgets
from django.contrib.auth.models import AbstractUser
from users import models as umod
from formlib.form import FormMixIn
from django.contrib.auth.decorators import permission_required

# add to your views
@view_function
@permission_required('users.add_exitsurvey', login_url='/users/login/')
def process_request(request):
    try:
        alumni = umod.User.objects.get(id=request.urlparams[0])
        #products = cmod.Product.objects.get(id=request.GET.get('id'))
    except umod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index')

    try:
        exit_survey = umod.ExitSurvey.objects.get(user = alumni)
        return HttpResponse('This alumni has already taken the exit survey')
    except umod.ExitSurvey.DoesNotExist:
        pass

    form = ExitForm(request)

    if form.is_valid():
        form.commit(alumni)
        return HttpResponseRedirect('/users/results/' + str(alumni.id))

    context = {
    'form': form,
    }

    return dmp_render(request, 'exit_survey.html', context)


class ExitForm(FormMixIn, forms.Form):

    def init(self):
        # Career Advisement Questions
        self.fields['career_advisor'] = forms.ModelChoiceField(label='Who was your Career Advisor?', queryset=umod.CareerAdvisor.objects.order_by('ca_first_name', 'ca_last_name').all())
        self.fields['ca_appointment'] = forms.ChoiceField(choices=umod.RATING, label='How many times did you meet with your Career Advisor?')
        self.fields['ca_help_rating'] = forms.ChoiceField(choices=umod.RATING, label='On a scale from 1 to 10, please rate the helpfulness of your career advisor. 1 being least helpful, 10 being most helpful')
        self.fields['ca_suggestions'] = forms.CharField(label='Do you have any suggestions about how your career advisor could be more helpful?', max_length=150, required=False)

        # Academic Advisement Questions
        self.fields['academic_advisor'] = forms.ModelChoiceField(label='Who was your Academic Advisor?', queryset=umod.AcademicAdvisor.objects.order_by('aa_first_name', 'aa_last_name').all())
        self.fields['aa_appointment'] = forms.ChoiceField(choices=umod.RATING, label="How many times did you meet with your Academic Advisor?")
        self.fields['aa_help_rating'] = forms.ChoiceField(choices=umod.RATING, label="On a scale from 1 to 10, please rate the helpfulness of your Academic Advisor. 1 being least helpful, 10 being most helpful")
        self.fields['aa_suggestions'] = forms.CharField(label="Do you have any suggestions about how your Academic Advisor could be more helpful?", max_length=150, required=False)

        # Program-related Questions
        self.fields['program'] = forms.ChoiceField(choices=umod.PROGRAM_CHOICES, label='What program are you currently in?')
        self.fields['program_introduction'] = forms.ChoiceField(choices=umod.INTRODUCTION_CHOICES, label="How did you learn about the Information Systems program?")
        self.fields['mism_decision'] = forms.CharField(label="Why did you decide to pursue the MISM?", max_length=130, required=False)
        self.fields['again'] = forms.ChoiceField(label="Given the opportunity to start over, would you choose IS again?", choices=umod.AGAIN_CHOICES)
        self.fields['again_response'] = forms.CharField(label="Please explain your response to the question above.", max_length=150, required=False)
        self.fields['additional_classes'] = forms.CharField(label="What classes or topics would you have liked to take that were not offered?", max_length=150, required=False)
        #this should be a drop down, not a radio selection
        self.fields['valuable_class'] = forms.ChoiceField(label="What was the most valuable class in the MISM?", choices=umod.VALUABLE_CHOICES)
        self.fields['valuable_class_response'] = forms.CharField(label="Please explain your response to the question above.", max_length=130, required=False)
        self.fields['least_valuable_class'] = forms.ChoiceField(label="What was the most valuable class in the MISM?", choices=umod.VALUABLE_CHOICES)
        self.fields['least_valuable_class_response'] = forms.CharField(label="Please explain your response to the question above.", max_length=150, required=False)
        self.fields['best_response'] = forms.CharField(label="What did you like best about the MISM and why?", max_length=150, required=False)
        self.fields['recommendation'] = forms.CharField(label="What recommendations would you make to improve the program?", max_length=150, required=False)

        # Donation Questions
        #this should be a drop down, not a radio selection
        self.fields['give_back'] = forms.ChoiceField(label="When you are able to do so, will you give back to the Information Systems program?", choices=umod.GIVE_CHOICES)
        self.fields['my_choice'] = forms.ChoiceField(label="""Did you participate in "My Choice to Give"?""", choices=umod.MY_CHOICE_CHOICES)
        self.fields['additional_comments'] = forms.CharField(label="Anything else you'd like us to know?", max_length=130, required=False)

    def commit(self, alumni):
        #######save program to user
        # program = umod.Program.objects.get(program_name = ['name'], career_advisor = ['career_advisor'], academic_advisor = ['academic_advisor'])
        # print(">>>>>>>>>>>>>", program)
        #user.save()
        #######save exit survey
        es = umod.ExitSurvey()
        es.user = alumni
        es.program_introduction = self.cleaned_data.get('program_introduction')
        es.mism_decision = self.cleaned_data.get('mism_decision')
        es.again = self.cleaned_data.get('again')
        es.again_response = self.cleaned_data.get('again_response')
        es.additional_classes = self.cleaned_data.get('additional_classes')
        es.valuable_class = self.cleaned_data.get('valuable_class')
        es.valuable_class_response = self.cleaned_data.get('valuable_class_response')
        es.least_valuable_class = self.cleaned_data.get('least_valuable_class')
        es.least_valuable_class_response = self.cleaned_data.get('least_valuable_class_response')
        es.best_response = self.cleaned_data.get('best_response')
        es.recommendation = self.cleaned_data.get('recommendation')
        es.response_date = self.cleaned_data.get('response_date')
        es.additional_comments = self.cleaned_data.get('additional_comments')
        es.academic_advisor = self.cleaned_data.get('academic_advisor')
        es.aa_appointment = self.cleaned_data.get('aa_appointment')
        es.aa_help_rating = self.cleaned_data.get('aa_help_rating')
        es.aa_suggestions = self.cleaned_data.get('aa_suggestions')
        es.career_advisor = self.cleaned_data.get('career_advisor')
        es.ca_appointment = self.cleaned_data.get('ca_appointment')
        es.ca_help_rating = self.cleaned_data.get('ca_help_rating')
        es.ca_suggestions = self.cleaned_data.get('ca_suggestions')
        es.save()
        #########save donation info
        d = umod.Donation()
        d.user = alumni
        d.give_back = self.cleaned_data.get('give_back')
        d.my_choice = self.cleaned_data.get('my_choice')
        d.save()
        ###########program Information
        alumni.program = self.cleaned_data.get('program')
        alumni.save()
