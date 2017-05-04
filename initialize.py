#!/usr/bin/env python3

from django.core import management
from django.db import connection
from datetime import datetime
import os, os.path, sys


# ensure the user really wants to do this
areyousure = input('''
  You are about to drop and recreate the entire database.
  All data are about to be deleted.  Use of this script
  may cause itching, vertigo, dizziness, tingling in
  extremities, loss of balance or coordination, slurred
  speech, temporary zoobie syndrome, longer lines at the
  testing center, changed passwords in Learning Suite, or
  uncertainty about whether to call your professor
  'Brother' or 'Doctor'.

  Please type 'yes' to confirm the data destruction: ''')
if areyousure.lower() != 'yes':
    print()
    print('  Wise choice.')
    sys.exit(1)

# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'AlumniDb.settings'
import django
django.setup()


# drop and recreate the database tables
print()
print('Living on the edge!  Dropping the current database tables.')
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")

# make the migrations and migrate
management.call_command('makemigrations')
management.call_command('migrate')


# imports for our project
from users import models as umod
from decimal import Decimal
import csv
from django.contrib.auth.models import Permission, Group

####Groups
g1 = Group()
g1.name = 'Alumni'
g1.save()
g1.permissions.add(Permission.objects.get(codename='add_company'))
g1.permissions.add(Permission.objects.get(codename='add_donation'))
g1.permissions.add(Permission.objects.get(codename='change_donation'))
g1.permissions.add(Permission.objects.get(codename='delete_donation'))
g1.permissions.add(Permission.objects.get(codename='add_exitsurvey'))
g1.permissions.add(Permission.objects.get(codename='add_fulltime'))
g1.permissions.add(Permission.objects.get(codename='change_fulltime'))
g1.permissions.add(Permission.objects.get(codename='delete_fulltime'))
g1.permissions.add(Permission.objects.get(codename='add_internship'))
g1.permissions.add(Permission.objects.get(codename='change_internship'))
g1.permissions.add(Permission.objects.get(codename='delete_internship'))
g1.permissions.add(Permission.objects.get(codename='add_offers'))
g1.permissions.add(Permission.objects.get(codename='change_offers'))
g1.permissions.add(Permission.objects.get(codename='delete_offers'))
g1.permissions.add(Permission.objects.get(codename='add_skills'))
g1.permissions.add(Permission.objects.get(codename='change_user'))
g1.save()

g2 = Group()
g2.name = 'Admin'
g2.save()
for p in Permission.objects.all():
    g2.permissions.add(Permission.objects.get(codename= p.codename))
g2.save()


#DUMMY DATA!
#advisors
ca1 = umod.CareerAdvisor()
ca1.ca_first_name = "Reid"
ca1.ca_last_name = "Grawe"
ca1.save()

aa1 = umod.AcademicAdvisor()
aa1.aa_first_name = "Caroline"
aa1.aa_last_name = "Thorne"
aa1.save()

#companies
c1 = umod.Company()
c1.name = "Adobe"
c1.city = "Lehi"
c1.state = "UT"
c1.save()

c2 = umod.Company()
c2.name = "LucidChart"
c2.city = "Lehi"
c2.state = "UT"
c2.save()

c3 = umod.Company()
c3.name = "Microsoft"
c3.city = "Seattle"
c3.state = "WA"
c3.save()

c4 = umod.Company()
c4.name = "Exxon"
c4.city = "Austin"
c4.state = "TX"
c4.save()

###############
#person stuff
#u1
u1 = umod.User()
u1.first_name = "Jennifer"
u1.last_name = "Luther"
u1.email = "luther.jenn@gmail.com"
u1.username = "luna"
u1.set_password("luther")
u1.alumni = False
u1.is_superuser=True
u1.save()

d1 = umod.Donation()
d1.give_back = "Money"
d1.my_choice = "Y"
d1.user = u1
d1.save()

i1 = umod.Internship()
i1.company = c1
i1.user = u1
i1.how_obtained = "I applied and rocked"
i1.hours_looking = '20'
i1.save()

f1 = umod.FullTime()
f1.company = c1
f1.user = u1
f1.date_accepted = "2018-02-25"
f1.expected_salary = Decimal('500000.00')
f1.position_title = "Security"
f1.contact = 'y'
f1.ft_hours_looking = '2'
f1.salary = Decimal('500000.00')
f1.position_description = "Being awesome"
f1.current_job = True
f1.start_date = "2018-05-25"
f1.end_date = "2050-05-25"
f1.avg_hours_week = '40'
f1.satisfaction = 'VS'
f1.projected_raise_time_months = '3'
f1.family_friendly = True
f1.family_friendly_response = "THey give my nonexistant kids icecream!"
f1.pros = "Icecream"
f1.cons = "I'm getting fat"
f1.save()

s1 = umod.Skills()
s1.full_time = f1
s1.skill = 'DA'
s1.save()

s2 = umod.Skills()
s2.full_time = f1
s2.skill = 'HD'
s2.save()

s3 = umod.Skills()
s3.full_time = f1
s3.skill = 'SD'
s3.save()

es1 = umod.ExitSurvey()
es1.user = u1
es1.program_introduction = "Bri Sorenson"
es1.mism_decision = "I wanted to get my masters"
es1.again = "Y"
es1.again_response = "It's so good!"
es1.additional_classes = "gymnasatics"
es1.valuable_class = "415"
es1.valuable_class_response = "good again"
es1.best_response = "Free food"
es1.recommendation = "paint nails"
es1.additional_comments = "yadda yadda yadda"
#career advisor response
es1.career_advisor = ca1
es1.ca_appointment = '5'
es1.ca_help_rating ='7'
es1.ca_suggestions = "Grow a beard"
#academic advisor response
es1.academic_advisor = aa1
es1.aa_appointment = '5'
es1.aa_help_rating = '7'
es1.aa_suggestions = "Grow a beard"
es1.save()

###############
#u2
u2 = umod.User()
u2.first_name = "Ashlyn"
u2.last_name = "Lewis"
u2.email = "lewis.ashlyn@gmail.com"
u2.username = "ashlyn"
u2.set_password("trashtan")
u2.alumni = False
u2.is_superuser=True
u2.save()

d2 = umod.Donation()
d2.give_back = "Both"
d2.my_choice = "N"
d2.user = u2
d2.save()

i2 = umod.Internship()
i2.company = c2
i2.user = u2
i2.how_obtained = "I'm obviously qualified more than anyone"
i2.hours_looking = '20'
i2.save()

f21 = umod.FullTime()
f21.company = c1
f21.user = u2
f21.date_accepted = "2014-02-25"
f21.expected_salary = Decimal('490000.00')
f21.position_title = "IT/Infra"
f21.contact = 'n'
f21.ft_hours_looking = '3'
f21.salary = Decimal('504500.00')
f21.position_description = "Drinking universe juice"
f21.current_job = False
f21.start_date = "2014-05-25"
f21.end_date = "2016-05-25"
f21.avg_hours_week = '26'
f21.satisfaction = 'S'
f21.projected_raise_time_months = '6'
f21.family_friendly = False
f21.family_friendly_response = "So much juice"
f21.pros = "Juice"
f21.cons = "Too much"
f21.save()

f22 = umod.FullTime()
f22.company = c3
f22.user = u2
f22.date_accepted = "2016-06-25"
f22.expected_salary = Decimal('670000.00')
f22.position_title = "Analytics"
f22.contact = 'y'
f22.ft_hours_looking = '15'
f22.salary = Decimal('670600.00')
f22.position_description = "Assure Quality"
f22.current_job = True
f22.start_date = "2016-07-25"
f22.avg_hours_week = '46'
f22.satisfaction = 'OK'
f22.projected_raise_time_months = '12'
f22.family_friendly = True
f22.family_friendly_response = "They are very accomadating"
f22.pros = "Family Friendly, good music"
f22.cons = "Bad temperature control"
f22.save()


s4 = umod.Skills()
s4.full_time = f21
s4.skill = 'AD'
s4.save()

s5 = umod.Skills()
s5.full_time = f21
s5.skill = 'ERP'
s5.save()

s6 = umod.Skills()
s6.full_time = f22
s6.skill = 'PDP'
s6.save()

es2 = umod.ExitSurvey()
es2.user = u2
es2.program_introduction = "Dan Moraine"
es2.mism_decision = "I was forced into it!"
es2.again = "Y"
es2.again_response = "By far the best major"
es2.additional_classes = "croque"
es2.valuable_class = "551"
es2.valuable_class_response = "Leading change has helped me so much"
es2.best_response = "Great people"
es2.recommendation = "hot air balloon rides"
es2.additional_comments = "cupcakes and jamba juice"
#career advisor response
es2.career_advisor = ca1
es2.ca_appointment = '2'
es2.ca_help_rating = '3'
es2.ca_suggestions = "Wonderful"
#academic advisor response
es2.academic_advisor = aa1
es2.aa_appointment = '6'
es2.aa_help_rating = '10'
es2.aa_suggestions = "So helpful"
es2.save()

###############
#u3
u3 = umod.User()
u3.first_name = "Emma"
u3.last_name = "Hayes"
u3.email = "isys-sec790@byu.edu"
u3.username = "emma"
u3.set_password("ilovejenn")
u3.alumni = False
u3.is_superuser=True
u3.save()

d3 = umod.Donation()
d3.give_back = "Time"
d3.my_choice = "Y"
d3.user = u3
d3.save()

i3 = umod.Internship()
i3.company = c1
i3.user = u3
i3.how_obtained = "I'm just the best.  Duh!"
i3.hours_looking = 1
i3.save()

f31 = umod.FullTime()
f31.company = c3
f31.user = u3
f31.date_accepted = "2016-02-25"
f31.expected_salary = Decimal('493000.00')
f31.position_title = "Data Science"
f31.contact = 'y'
f31.ft_hours_looking = '5'
f31.salary = Decimal('504500.00')
f31.position_description = "Wildlife and tech stuff"
f31.current_job = True
f31.start_date = "2016-05-25"
f31.avg_hours_week = 35
f31.satisfaction = 'VS'
f31.projected_raise_time_months = '2'
f31.family_friendly = True
f31.family_friendly_response = "They let my kids come to work with me"
f31.pros = "Understanding and flexible with time"
f31.cons = "Long Commute"
f31.save()

f32 = umod.FullTime()
f32.company = c2
f32.user = u3
f32.date_accepted = "2013-06-25"
f32.expected_salary = Decimal('670000.00')
f32.position_title = "Project"
f32.contact = 'n'
f32.ft_hours_looking = '6'
f32.salary = Decimal('65123.00')
f32.position_description = "Assure Quality in the engineering department"
f32.current_job = False
f32.start_date = "2013-07-25"
f32.end_date = "2013-05-25"
f32.avg_hours_week = '46'
f32.satisfaction = 'D'
f32.projected_raise_time_months = '12'
f32.family_friendly = True
f32.family_friendly_response = "They are very accomadating"
f32.pros = "Family Friendly, good music"
f32.cons = "Bad temperature control"
f32.save()

f33 = umod.FullTime()
f33.company = c1
f33.user = u3
f33.date_accepted = "2014-06-25"
f33.expected_salary = Decimal('670000.00')
f33.position_title = "Mobile/Web Dev"
f33.contact = 'y'
f33.ft_hours_looking = '15'
f33.salary = Decimal('670600.00')
f33.position_description = "Assure Quality in the engineering department"
f33.current_job = False
f33.start_date = "2014-07-25"
f33.end_date = "2015-05-25"
f33.avg_hours_week = '43'
f33.satisfaction = 'S'
f33.projected_raise_time_months = '4'
f33.family_friendly = True
f33.family_friendly_response = "They are very accomadating"
f33.pros = "Family Friendly, good music"
f33.cons = "Bad water"
f33.save()


s7 = umod.Skills()
s7.full_time = f31
s7.skill = 'IS'
s7.save()

s8 = umod.Skills()
s8.full_time = f31
s8.skill = 'GA'
s8.save()

s9 = umod.Skills()
s9.full_time = f32
s9.skill = 'CFS'
s9.save()

s10 = umod.Skills()
s10.full_time = f33
s10.skill = 'WB'
s10.save()

s11 = umod.Skills()
s11.full_time = f33
s11.skill = 'PP'
s11.save()

es2 = umod.ExitSurvey()
es2.user = u3
es2.program_introduction = "Major Fair"
es2.mism_decision = "MSISM Projects"
es2.again = "Y"
es2.again_response = "By far the best major"
es2.additional_classes = "smoothie making"
es2.valuable_class = "562"
es2.valuable_class_response = "Project Management was so helpful"
es2.best_response = "Great knowledge available"
es2.recommendation = "free cars for everyone"
#career advisor response
es2.career_advisor = ca1
es2.ca_appointment = '6'
es2.ca_help_rating = '8'
es2.ca_suggestions = "Very good"
#academic advisor response
es2.academic_advisor = aa1
es2.aa_appointment = '6'
es2.aa_help_rating = '7'
es2.aa_suggestions = "So helpful"
es2.save()
