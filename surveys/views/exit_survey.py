from django import forms
from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django.forms import widgets
from django.contrib.auth.models import AbstractUser
from users import models as umod


# add to your views
@view_function
def exitsurvey(request):

    form = ExitForm()
    if request.method == 'POST':
        form = ExitForm(request.POST)
        if form.is_valid():

            #need to first filter on user, and select that user

            # create objects for each type of models
            d = umod.Donation()
            i = umod.Internship()
            c = umod.company()
            ft = umod.FullTime()
            cft = umod.CompanyFullTime()
            ca = umod.CareerAdvisor()
            car = umod.CareerAdvisorResponse()
            aa = umod.AcademicAdvisor()
            aar = AcademicAdvisorResponse()
            p = umod.program()
            pr = umod.ProgramResponse()

            # fill objects with data from the form
            d.give_back = form.cleaned_data.get('give_back')
            d.my_choice = form.cleaned_data.get('my_choice')

            i.company_name = form.cleaned_data.get('company_name')
            i.how_obtained = form.cleaned_data.get('how_obtained')

            pi.time_looking = form.cleaned_data.get('time_looking')

            c.name = form.cleaned_data.get('name')
            c.city = form.cleaned_data.get('city')
            c.state = form.cleaned_data.get('state')

            ft.offers_received = form.cleaned_data.get('offers_received')
            ft.date_accepted = form.cleaned_data.get('date_accepted')
            ft.expected_salary = form.cleaned_data.get('expected_salary')
            ft.position_title = form.cleaned_data.get('position_title')
            ft.contact = form.cleaned_data.get('contact')
            ft.salary = form.cleaned_data.get('salary')
            ft.position_description = form.cleaned_data.get('position_description')
            ft.accepted_offer = form.cleaned_data.get('accepted_offer')

            ca.ca_first_name = form.cleaned_data.get('ca_first_name')
            ca.ca_last_name = form.cleaned_data.get('ca_last_name')

            car.ca_appointment = form.cleaned_data.get('appointment')
            car.ca_help_rating = form.cleaned_data.get('help_rating')
            car.ca_suggestions = form.cleaned_data.get('suggestions')

            aa.aa_first_name = form.cleaned_data.get('aa_first_name')
            aa.aa_last_name = form.cleaned_data.get('aa_last_name')

            aar.aa_appointment = form.cleaned_data.get('appointment')
            aar.aa_help_rating = form.cleaned_data.get('help_rating')
            aar.aa_suggestions = form.cleaned_data.get('suggestions')

            p.name = form.cleaned_data.get('name')

            pr.program_introduction = form.cleaned_data.get('program_introduction')
            pr.mism_decision = form.cleaned_data.get('mism_decision')
            pr.again = form.cleaned_data.get('again')
            pr.again_response = form.cleaned_data.get('again_response')
            pr.additional_classes = form.cleaned_data.get('additional_classes')
            pr.valuable_class = form.cleaned_data.get('valuable_class')
            pr.valuable_class_response = form.cleaned_data.get('valuable_class_response')
            pr.least_valuable_class = form.cleaned_data.get('valuable_class')
            pr.least_valuable_class_response = form.cleaned_data.get('valuable_class_response')
            pr.best_response = form.cleaned_data.get('best_response')
            pr.recommendation = form.cleaned_data.get('recommendation')
            pr.response_date = form.cleaned_data.get('response_date')
            pr.additional_comments = form.cleaned_data.get('additional_comments')


            # Inserts into models
            d.save()
            i.save()
            pi.save()
            c.save()
            ft.save()
            cft.save()
            ca.save()
            car.save()
            aa.save()
            aar.save()
            p.save()
            pr.save()

            return HttpResponseRedirect('/surveys/index/')

    template_vars = {
    'form': form,
    }

    return dmp_render(request, 'exit_survey.html', template_vars)


class ExitForm(forms.Form):

    # Choice LISTS
    TIME_RANGE = [
        ('0-10', '0 - 10 Hours'),
        ('10-20', '10 - 20 Hours'),
        ('20-30', '20 - 30 Hours'),
        ('40-60', '40 - 60 Hours'),
        ('60+', '60+ Hours'),
    ]

    NUM_OFFERS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('No Offer', 'I have not received an offer yet.'),
        ('Not Accepted Yet', 'I received an offer(s), but have not yet accepted.'),
    ]

    AGAIN_CHOICES = [
        ('Y', "Yes"),
        ("N", "No"),
        ("NS", "Not Sure"),
    ]

    VALUABLE_CHOICES =[
        ("415", "IS 415 (Capstone)"),
        ("531", "IS 531 (Enterprise Infrastructure)"),
        ("550/552", "IS 550/552 (Capstone)"),
        ("551", "IS 551 (Leading Change)"),
        ("555", "IS 555 (BI)"),
        ("560", "IS 560 (Security)"),
        ("562", "IS 562 (Project Management)"),
        ("Other", "Other"),
    ]

    GIVE_CHOICES = [
        ("Money", "Money (donations to department, scholarship funds, etc.)"),
        ("Time", "Time (mentorship, guest lectures, etc.)"),
        ("Both", "Both"),
        ("No", "I don't plan on giving back"),
    ]

    MY_CHOICE_CHOICES = [
        ("Y", "Yes"),
        ("N", "No"),
    ]



    response_date = forms.DateField(label='Date:', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={"class":"form-control"}))

    # Internship Questions
    internship_flag = forms.BooleanField(label='Did you complete an internship?', required=True)
    company_name = forms.CharField(label='What is the name of the company you interned with?')
    city = forms.CharField(label='In what city did you intern?')
    state = forms.CharField(label='In what state did you intern?')
    how_obtained = forms.CharField(label='How did you obtain your internship?')
    time_looking = forms.IntegerField(label='How much time did you spend looking for your internship?', choices=TIME_RANGE)

    # Full-Time Questions
    offers_received = forms.ChoiceField(label='How many full-time offers did you receive?', required=True, widget=forms.Select(attrs={"class":"form-control"}), choices=NUM_OFFERS)
    #Can I make accepted_offer show my company table information?
    accepted_offer = forms.IntegerField(label='Which company did you accept an offer with?', required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    date_accepted = forms.DateField(label='When did you accept this offer?')
    expected_salary = forms.DecimalField(label='What is your expected salary?', max_digits=6, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    position_title = forms.CharField(label='What is your position title?', max_length=40, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    position_description = forms.CharField(label='Which of the following best describes your position?', max_length=40, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    #if other, list here:  ##how do I do that?##
    #drop down from choices in models.py? I tried, and I think it looks good but I'm not sure how right it is
    contact = forms.MultipleChoiceField(label="Are you willing to serve as a contact for the company you've selected?", max_length=1, required=True, widget=forms.Select(attrs={"class":"form-control"}), choices=CONTACT_CHOICES)
    time_looking = forms.CharField(label="How much time did you spend looking for your full-time position?", max_length=20, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))

    # Career Advisement Questions
    ca_first_name = forms.CharField(label='What is the first name of your Career Advisor?')
    ca_last_name = forms.CharField(label='What is the last name of your Career Advisor?')
    appointment = forms.IntegerField(label='How many times did you meet with your Career Advisor?')
    help_rating = forms.ChoiceField(label='On a scale from 1 to 10, please rate the helpfulness of your career advisor. 1 being least helpful, 10 being most helpful')
    suggestions = forms.CharField(label='Do you have any suggestions about how your career advisor could be more helpful?')

    # Academic Advisement Questions
    aa_first_name = forms.CharField(label='What is the first name of your Career Advisor?')
    aa_last_name = forms.CharField(label='What is the last name of your Career Advisor?')
    #this should be a drop down, not a radio selection
    appointment = forms.CharField(label="How many times did you meet with your academic advisor?", max_length=2, required=True, widget=forms.Select(attrs={"class":"form-control"}), choices=[(x,x) for x in range(1,5)])
    help_rating = forms.CharField(label="Please rate Caroline's helpfulness in your search for an internship/full-time position.", max_length=2, required=True, widget=forms.Select(attrs={"class":"form-control"}), choices=[(x,x) for x in range(1,10)])
    suggestions = forms.CharField(label="What suggestion would you give to Caroline to help her improve?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))

    # Program-related Questions
    name = forms.CharField(label='What program are you currently in?')
    program_introduction = forms.CharField(label="How did you learn about the Information Systems program?", max_length=40, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    mism_decision = forms.CharField(label="Why did you decide to pursue the MISM?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    again = forms.CharField(label="Given the opportunity to start over, would you choose IS again?", max_length=2, required=True, widget=forms.Select(attrs={"class":"form-control"}), choices=AGAIN_CHOICES)
    again_response = forms.CharField(label="Please explain your response to the question above.", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    additional_classes = forms.CharField(label="What classes or topics would you have liked to take that were not offered?", max_length=10, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    #this should be a drop down, not a radio selection
    valuable_class = forms.CharField(label="What was the most valuable class in the MISM?", max_length=2, required=True, widget=forms.Select(attrs={"class":"form-control"}), choices=VALUABLE_CHOICES)
    valuable_class_response = forms.CharField(label="Please explain your response to the question above.", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    least_valuable_class = forms.CharField(label="What was the most valuable class in the MISM?", max_length=2, required=True, widget=forms.Select(attrs={"class":"form-control"}), choices=VALUABLE_CHOICES)
    least_valuable_class_response = forms.CharField(label="Please explain your response to the question above.", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    best_response = forms.CharField(label="What did you like best about the MISM and why?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    recommendation = forms.CharField(label="What recommendations would you make to improve the program?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))

    # Donation Questions
    #this should be a drop down, not a radio selection
    give_back = forms.CharField(label="When you are able to do so, will you give back to the Information Systems program?", max_length=2, required=True, widget=forms.RadioSelect(attrs={"class":"form-control"}), choices=GIVE_CHIOCES)
    give_back = forms.CharField(label="""Did you participate in "My Choice to Give"?""", max_length=2, required=True, widget=forms.RadioSelect(attrs={"class":"form-control"}), choices=MY_CHOICE_CHOICES)
    additional_comments = forms.CharField(label="Anything else you'd like us to know?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
