from django.db import models
from django.core.validators import MaxValueValidator
# LISTS
TIME_RANGE = [
    ('0 - 10 Hours'),
    ('10 - 20 Hours'),
    ('20 - 30 Hours'),
    ('40 - 60 Hours'),
    ('60+ Hours'),
]

VALUABLE = [
    ('IS 415 (Capstone)'),
    ('IS 531 (Enterprise Infrastructure)'),
    ('IS 550/552 (Capstone)'),
    ('IS 551 (Leading Change)'),
    ('IS 555 (BI)'),
    ('IS 560 (Security)'),
    ('IS 562 (Project Management)'),
    ('Other'),
]

PROGRAM_INTRO = [
    ('Students in the program'),
    ('Family member'),
    ('Alumni'),
    ('School counselor'),
    ('Online'),
    ('Advertisement'),
    ('Information Session'),
    ('IS 201'),
    ('Other'),
]

STATE = [
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
]

# Define models here


class Person(models.Model):
    # an id field should be created and made the primary key
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, null=True)
    internship_flag = models.BooleanField(blank=True)
    additional_comments = models.CharField(
        max_length=254, null=True, blank=True)


class Donation(models.Model):
    # this model tracks whether the person submits a Donation
    give_back = models.CharField(max_length=30)
    my_choice = models.BooleanField(blank=True)
    person = models.ForeignKey('Person')


class Internship(models.Model):
    company_name = models.CharField(max_length=30)
    how_obtained = models.CharField(max_length=40)


class PersonInternship(models.Model):
    person = models.ForeignKey('Person')
    internship = models.ForeignKey('Internship')
    time_looking = models.IntegerField(null=True, blank=True)



class Company(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2, choices=STATE)


class FullTime(models.Model):
    offers_received = models.IntegerField(null=True, blank=True)
    date_accepted = models.DateField()
    expected_salary = models.DecimalField(max_digits=6, decimal_places=2)
    position_title = models.CharField(max_length=30)
    # this field is to see if the person
    contact = models.CharField(max_length=1)
    # is willing to be a contact for the company
    # y=yes, n=no, m=maybe
    time_looking = models.IntegerField(null=True, blank=True)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    position_description = models.CharField(max_length=30)
    difficulties = models.CharField(max_length=150)
    accepted_offer = models.ForeignKey('Company')
    person_id = models.ForeignKey('Person')


class CompanyFullTime(models.Model):
    company = models.ForeignKey('Company')
    full_time = models.ForeignKey('FullTime')


class CareerAdvisor(models.Model):
    ca_first_name = models.CharField(max_length=30)
    ca_last_name = models.CharField(max_length=30)


class CareerAdvisorResponse(models.Model):
    career_advisor = models.ForeignKey('CareerAdvisor')
    appointment = models.IntegerField()  # number of times they've had appointments
    help_rating = models.IntegerField()  # rating of advisors helpfulness
    suggestions = models.CharField(max_length=150)


class AcademicAdvisor(models.Model):
    aa_first_name = models.CharField(max_length=30)
    aa_last_name = models.CharField(max_length=30)


class AcademicAdvisorResponse(models.Model):
    academic_advisor = models.ForeignKey('AcademicAdvisor')
    appointment = models.IntegerField()  # number of times they've had appointments
    help_rating = models.IntegerField()  # rating of advisors helpfulness
    suggestions = models.CharField(max_length=150)


class Program(models.Model):
    career_advisor = models.ForeignKey('CareerAdvisor')
    academic_advisor = models.ForeignKey('AcademicAdvisor')
    name = models.CharField(max_length=30)


class ProgramResponse(models.Model):
    program = models.ForeignKey('Program')
    person = models.ForeignKey('Person')
    program_introduction = models.CharField(max_length=30)
    mism_decision = models.CharField(max_length=30)
    # Given the opportunity to start over, would you choose IS again?
    again = models.CharField(max_length=10)
    again_response = models.CharField(max_length=150, null=True, blank=True)
    additional_classes = models.CharField(
        max_length=150, null=True, blank=True)
    valuable_class = models.CharField(max_length=30, null=True, blank=True)
    valuable_class_response = models.CharField(
        max_length=150, null=True, blank=True)
    # what did you like best about the MISM and why?
    best_response = models.CharField(max_length=150, null=True, blank=True)
    recommendation = models.CharField(max_length=150, null=True, blank=True)
    response_date = models.DateTimeField(null=True, blank=True)
    additional_comments = models.CharField(
        max_length=150, null=True, blank=True)
