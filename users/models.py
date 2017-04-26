
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser
# LISTS

PROGRAM_CHOICES = [
    ('MISM', 'Masters of Information Systems Management'),
    ('BSIS', 'Bachelors of Information Systems'),
]

RATING = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
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

Academic_Advisors = [
    ('Caroline', 'Caroline Thorne'),
    ('-', '-'),
]

## in the list above, we might consider putting in the undergrad advisor
## I don't remember who it is, but if we ever collect BSIS data, we'd want that


Career_Advisors = [
    ('Reid', 'Reid Grawe'),
    ('-', '-'),
]

TIME_RANGE = [
    ('0-10', '0 - 10 Hours'),
    ('10-20', '10 - 20 Hours'),
    ('20-30', '20 - 30 Hours'),
    ('40-60', '40 - 60 Hours'),
    ('60+', '60+ Hours'),
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

CONTACT_CHOICES = [
    ('Y', "Yes"),
    ("N", "No"),
    ("M", "Maybe"),
]

AGAIN_CHOICES = [
    ('Y', "Yes"),
    ("N", "No"),
    ("NS", "Not Sure"),
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

INTRODUCTION_CHOICES = [
    ("1", "Student in the program"),
    ("2", "Family member"),
    ("3", "Alumni"),
    ("4", "School counselor"),
    ("5", "Online"),
    ("6", "Advertisement"),
    ("7", "Information Session"),
    ("8", "IS 201"),
    ("9", "Other"),
]

POSITION_CHOICES =[
    ('BI/Db', 'BI/Database'),
    ('Consulting', 'Consulting'),
    ('IT/Infra', 'IT/Infrastructure'),
    ('Software Engineering', 'Software Engineering'),
    ('Mobile/Web Dev', 'Mobile/Web Development'),
    ('Security', 'Security'),
    ('Analytics', 'Analytics'),
    ('Data Science', 'Data Science'),
    ('Project', 'Project Management'),
    ('IT Audit', 'IT Audit'),
    ('Security Audit', 'Security Audit'),
    ('Other', 'Other'),
]

SATISFACTION_CHOICES = [
    ('VS', 'Very Satisfied'),
    ('S', 'Satisfied'),
    ('OK', 'Ok'),
    ('D', 'Disatisfied'),
    ('VD', 'Very Disatisfied'),
]

SKILLS_CHOICES = [
    ('AD', 'Algorithm Design'),
    ('BPC', 'Business Processes and Controls'),
    ('CFS', 'Computing Foundational Skills'),
    ('DA', 'Database Analysis'),
    ('DS', 'Database Systems'),
    ('EI', 'Enterprise Infrastructure'),
    ('ERP', 'ERP Systems'),
    ('GA', 'Graphics and Animation'),
    ('HD', 'Hardware Design'),
    ('IP', 'Image Processing'),
    ('IS', 'Information Security'),
    ('MO', 'Microsoft Office'),
    ('NM', 'Numerical Method'),
    ('P', 'Platforms'),
    ('PDP', 'Product Design and Production'),
    ('PLE', 'Programming Languages/Environments'),
    ('PP', 'Programming Paradigms'),
    ('PS', 'Psychology of Security'),
    ('SD', 'Software Design'),
    ('SDM', 'Software Development Methodologies'),
    ('SDT', 'Software Development Tools'),
    ('ST', 'Software Testing'),
    ('S', 'Statistics'),
    ('SN', 'System Networks'),
    ('T', 'Theory'),
    ('WB', 'Web Design'),
]

# Define models here


class User(AbstractUser):
    # an id field should be created and made the primary key
    #id
    #first_name
    #last_name
    #email
    #username
    #password
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=2, choices=STATE, blank=True, null=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    graduationDate = models.DateField(null=True, blank=True)

class Donation(models.Model):
    # this model tracks whether the person submits a Donation
    give_back = models.CharField(max_length=5, null=True, blank=True, choices=GIVE_CHOICES)
    my_choice = models.CharField(max_length=1, null=True, blank=True, choices=MY_CHOICE_CHOICES)
    user = models.ForeignKey('User')

class Company(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, )
    city = models.CharField(max_length=30, null=True, blank=True, )
    state = models.CharField(max_length=2, choices=STATE)

    def __str__(self):
        return self.name + " (" + self.city + ", " + self.state + ")"

    class Meta:
        unique_together = ["name", "city", "state"]

class Internship(models.Model):
    company = models.ForeignKey('Company', null=True, blank=True)
    user = models.ForeignKey('User', null=True, blank=True)
    how_obtained = models.CharField(max_length=40, null=True, blank=True)
    hours_looking = models.IntegerField(null=True, blank=True)
    position_title = models.CharField(null=True, blank=True, max_length=30)

class FullTime(models.Model):
    company = models.ForeignKey('Company') #can we make the choices come from the company table?
    user = models.ForeignKey('User')

    date_accepted = models.DateField(null=True, blank=True)
    expected_salary = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=2)
    position_title = models.CharField(null=True, blank=True, max_length=30)
    # this field is to see if the person is willing to be a contact for the company
    contact = models.CharField(max_length=1, null=True, blank=True, choices=CONTACT_CHOICES)
    ft_hours_looking = models.IntegerField(null=True, blank=True, choices=TIME_RANGE)
    salary = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    position_description = models.CharField(null=True, blank=True, max_length=150)
    current_job = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    avg_hours_week = models.IntegerField(null=True, blank=True)
    satisfaction = models.CharField(max_length=50, null=True, blank=True, choices=SATISFACTION_CHOICES)
    projected_raise_time_months = models.IntegerField(null=True, blank=True)
    family_friendly = models.BooleanField(default=False)
    family_friendly_response = models.CharField(max_length=200, null=True, blank=True)
    pros = models.CharField(max_length=200, null=True, blank=True)
    cons = models.CharField(max_length=200, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Offers(models.Model):
    company = models.ForeignKey('Company')
    user = models.ForeignKey('User')
    intern_offer = models.BooleanField(default=False)

class Skills(models.Model):
    full_time = models.ForeignKey('FullTime')
    skill = models.CharField(max_length=50, choices=SKILLS_CHOICES)


class CareerAdvisor(models.Model):
    ca_first_name = models.CharField(null=True, blank=True, max_length=30)
    ca_last_name = models.CharField(null=True, blank=True, max_length=30)


class AcademicAdvisor(models.Model):
    aa_first_name = models.CharField(null=True, blank=True, max_length=30)
    aa_last_name = models.CharField(null=True, blank=True, max_length=30)


class Program(models.Model):
    career_advisor = models.ForeignKey('CareerAdvisor')
    academic_advisor = models.ForeignKey('AcademicAdvisor')
    program_name = models.CharField(max_length=4, null=True, blank=True, choices=PROGRAM_CHOICES)


class ExitSurvey(models.Model):
    user = models.ForeignKey('User')
    program_introduction = models.CharField(null=True, blank=True, max_length=30, choices=INTRODUCTION_CHOICES)
    mism_decision = models.CharField(null=True, blank=True, max_length=130)
    # Given the opportunity to start over, would you choose IS again?
    again = models.CharField(null=True, blank=True, max_length=2, choices=AGAIN_CHOICES)
    again_response = models.CharField(max_length=150, null=True, blank=True)
    additional_classes = models.CharField(max_length=150, null=True, blank=True)
    valuable_class = models.CharField(max_length=30, null=True, blank=True, choices=VALUABLE_CHOICES)
    valuable_class_response = models.CharField(max_length=150, null=True, blank=True)
    least_valuable_class = models.CharField(max_length=30, null=True, blank=True, choices=VALUABLE_CHOICES)
    least_valuable_class_response = models.CharField(max_length=150, null=True, blank=True)
    # what did you like best about the MISM and why?
    best_response = models.CharField(max_length=150, null=True, blank=True)
    recommendation = models.CharField(max_length=150, null=True, blank=True)
    response_date = models.DateTimeField(auto_now_add=True)
    additional_comments = models.CharField( max_length=150, null=True, blank=True)
    #Academic Advisor Responses
    academic_advisor = models.ForeignKey('AcademicAdvisor')
    aa_appointment = models.IntegerField(null=True, blank=True)  # number of times they've had appointments
    aa_help_rating = models.IntegerField(null=True, blank=True, choices=RATING)  # rating of advisors helpfulness
    aa_suggestions = models.CharField(null=True, blank=True, max_length=150)
    #Career Advisor Responses
    career_advisor = models.ForeignKey('CareerAdvisor')
    ca_appointment = models.IntegerField(null=True, blank=True)  # number of times they've had appointments
    ca_help_rating = models.IntegerField(null=True, blank=True, choices=RATING)  # rating of advisors helpfulness
    ca_suggestions = models.CharField(null=True, blank=True, max_length=150)

class ReocurringSurvey(models.Model):
    user = models.ForeignKey('User')
    valuable_program_info = models.CharField(max_length=150, null=True, blank=True)
