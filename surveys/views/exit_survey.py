from django import forms
from .models import Post
from django.conf import settings
from users import models as umod
from django.forms import widgets
from django.contrib.auth.models import AbstractUser


# add to your views
@view_function
def jobinformation(request):
    form = ExitForm()
    if request.method == 'POST':
        form = ExitForm(request.POST)

    template_vars = {
    'form': form,
    }

    return dmp_render_to_response(request, 'exit_survey', template_vars)

@view_function
def programinformation(request):
    form = ExitForm()
    if request.method == 'POST':
        form = ExitForm(request.POST)

    template_vars = {
    'form': form,
    }

    return dmp_render_to_response(request, 'exit_survey', template_vars)

    # our new form
class JobInformation(forms.Form): #using users.FullTime
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    offers_received = forms.IntegerField(label='How many full-time offers did you receive?', required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    #Can I make accepted_offer show my company table information?
    accepted_offer = forms.IntegerField(label='Which company did you accept an offer with?', required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    expected_salary = forms.DecimalField(label='What is your expected salary?', max_digits=6, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    position_title = forms.CharField(label='What is your position title?', max_length=40, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    position_description = forms.CharField(label='Which of the following best describes your position?', max_length=40, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    #if other, list here:  ##how do I do that?
    #drop down from choices in models.py? I tried, and I think it looks good but I'm not sure how right it is
    contact = forms.MultipleChoiceField(label="Are you willing to serve as a contact for the company you've selected?", max_length=1, required=True, widget=forms.RadioSelect(attrs={"class":"form-control"}), choices=CONTACT_CHOICES)
    time_looking = forms.CharField(label="How much time did you spend looking for your full-time position?", max_length=20, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))


class ProgramInformation(forms.Form):
    program_introduction = forms.CharField(label="How did you learn about the Information Systems program?", max_length=40, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    mism_decision = forms.CharField(label="Why did you decide to pursue the MISM?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    again = forms.CharField(label="Given the opportunity to start over, would you choose IS again?", max_length=2, required=True, widget=forms.RadioSelect(attrs={"class":"form-control"}), choices=AGAIN_CHOICES)
    again_response = forms.CharField(label="Please explain your response to the question above.", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    additional_classes = forms.CharField(label="What classes or topics would you have liked to take that were not offered?", max_length=10, required=True, widget=forms.(attrs={"class":"form-control"}))
    #this should be a drop down, not a radio selection
    valuable_class = forms.CharField(label="What was the most valuable class in the MISM?", max_length=2, required=True, widget=forms.RadioSelect(attrs={"class":"form-control"}), choices=VALUABLE_CHOICES)
    valuable_class_response = forms.CharField(label="Please explain your response to the question above.", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    best_response = forms.CharField(label="What did you like best about the MISM and why?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    recommendation = forms.CharField(label="What recommendations would you make to improve the program?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    #this should be a drop down, not a radio selection
    appointment = forms.CharField(label="How many times did you meet with Caroline?", max_length=2, required=True, widget=forms.RadioSelect(attrs={"class":"form-control"}), choices=[(x,x) for x in range(1,5)])
    help_rating = forms.CharField(label="Please rate Caroline's helpfulness in your search for an internship/full-time position.", max_length=2, required=True, widget=forms.RadioSelect(attrs={"class":"form-control"}), choices=[(x,x) for x in range(1,10)])
    suggestions = forms.CharField(label="What suggestion would you give to Caroline to help her improve?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
    #this should be a drop down, not a radio selection
    give_back = forms.CharField(label="When you are able to do so, will you give back to the Information Systems program?", max_length=2, required=True, widget=forms.RadioSelect(attrs={"class":"form-control"}), choices=GIVE_CHIOCES)
    give_back = forms.CharField(label="""Did you participate in "My Choice to Give"?""", max_length=2, required=True, widget=forms.RadioSelect(attrs={"class":"form-control"}), choices=MY_CHOICE_CHOICES)
    additional_comments = forms.CharField(label="Anything else you'd like us to know?", max_length=130, required=True, widget=forms.Textarea(attrs={"class":"form-control"}))
