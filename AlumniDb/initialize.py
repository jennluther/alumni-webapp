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

#DUMMY DATA!
#advisors
ca1 = umod.CareerAdvisor()
ca1.ca_first_name = "Reid"
ca1.ca_last_name = "Grawe"

aa1 = umod.CareerAdvisor()
aa1.aa_first_name = "Caroline"
aa1.aa_last_name = "Thorne"

#companies
c1 = umod.Company()
c1.name = "Adobe"
c1.city = "Lehi"
c1.state = "UT"

c2 = umod.Company()
c2.name = "LucidChart"
c2.city = "Lehi"
c2.state = "UT"

c3 = umod.Company()
c3.name = "Microsoft"
c3.city = "Seattle"
c3.state = "WA"

c4 = umod.Company()
c4.name = "Exxon"
c4.city = "Austin"
c4.state = "TX"

###############
#person stuff
#u1
u1 = User()
u1.first_name = "Jennifer"
u1.last_name = "Luther"
u1.email = "luther.jenn@gmail.com"
u1.username = "luna"
u1.set_password("luther")
u1.city = "Springville"
u1.state = "UT"
u1.phone = 8013586330
u1.graduationDate = "2018-4-25 14:30:59"
u1.save()

d1 = Donation()
d1.give_back = "I will give back"
d1.my_choice = "My choice is great"
d1.user = u1
d1.save()

i1 = Internship()
i1.company = c1
i1.user = u1
i1.how_obtained = "I applied and rocked"
i1.hours_looking = 20

f1 = FullTime()
f1.company = c1
f1.user = u1
f1.date_accepted = "2018-2-25 14:30:59"
f1.expected_salary = 500000.00
f1.position_title = "Security"
f1.contact = y
f1.ft_hours_looking = 2
f1.salary = 500000.00
f1.position_description = "Being awesome"
f1.current_job = True
f1.start_date = "2018-5-25 14:30:59"
f1.end_date = "2050-5-25 14:30:59"
f1.avg_hours_week = 40
f1.satisfaction = VS
f1.projected_raise_time_months = 3
f1.family_friendly = True
f1.family_friendly_response = "THey give my nonexistant kids icecream!"
f1.pros = "Icecream"
f1.cons = "I'm getting fat"

cft1 = CompanyFullTime()
cft1.company = c1
cft1.full_time = f1

s1 = Skills()
s1.full_time = f1
s1.skill = 'DA'

s2 = Skills()
s2.full_time = f1
s2.skill = 'HD'

s3 = Skills()
s3.full_time = f1
s3.skill = 'SD'

es1 = ExitSurvey()
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
es1.ca_appointment = 5
es1.ca_help_rating = 7
es1.ca_suggestions = "Grow a beard"
#academic advisor response
es1.academic_advisor = aa1
es1.aa_appointment = 5
es1.aa_help_rating = 7
es1.aa_suggestions = "Grow a beard"

###############
#u2
u2 = User()
u2.first_name = "Ashlyn"
u2.last_name = "Lewis"
u2.email = "lewis.ashlyn@gmail.com"
u2.username = "bomb"
u2.set_password("trashtan")
u2.city = "Spanish Fork"
u2.state = "UT"
u2.phone = 8015469865
u2.graduationDate = "2019-4-25 14:30:59"
u2.save()

d2 = Donation()
d2.give_back = "sure"
d2.my_choice = "I give to my choice all the time"
d2.user = u2
d2.save()

i2 = Internship()
i2.company = c2
i2.user = u2
i2.how_obtained = "I'm obviously qualified more than anyone"
i2.hours_looking = 20

f21 = FullTime()
f21.company = c1
f21.user = u2
f21.date_accepted = "2014-2-25 14:30:59"
f21.expected_salary = 490000.00
f21.position_title = "IT/Infra"
f21.contact = n
f21.ft_hours_looking = 3
f21.salary = 504500.00
f21.position_description = "Drinking universe juice"
f21.current_job = False
f21.start_date = "2014-5-25 14:30:59"
f21.end_date = "2016-5-25 14:30:59"
f21.avg_hours_week = 26
f21.satisfaction = S
f21.projected_raise_time_months = 6
f21.family_friendly = False
f21.family_friendly_response = "So much juice"
f21.pros = "Juice"
f21.cons = "Too much"

f22 = FullTime()
f22.company = c3
f22.user = u2
f22.date_accepted = "2016-6-25 14:30:59"
f22.expected_salary = 670000.00
f22.position_title = "Analytics"
f22.contact = y
f22.ft_hours_looking = 15
f22.salary = 670600.00
f22.position_description = "Assure Quality in the engineering department"
f22.current_job = True
f22.start_date = "2016-7-25 14:30:59"
f22.avg_hours_week = 46
f22.satisfaction = OK
f22.projected_raise_time_months = 12
f22.family_friendly = True
f22.family_friendly_response = "They are very accomadating"
f22.pros = "Family Friendly, good music"
f22.cons = "Bad temperature control"


s4 = Skills()
s4.full_time = f21
s4.skill = 'AD'

s5 = Skills()
s5.full_time = f21
s5.skill = 'ERP'

s6 = Skills()
s6.full_time = f22
s6.skill = 'PDP'

es2 = ExitSurvey()
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
es2.ca_appointment = 2
es2.ca_help_rating = 3
es2.ca_suggestions = "Wonderful"
#academic advisor response
es2.academic_advisor = aa1
es2.aa_appointment = 6
es2.aa_help_rating = 10
es2.aa_suggestions = "So helpful"

###############
#u3
u3 = User()
u3.first_name = "Nic"
u3.last_name = "Anderson"
u3.email = "nicvanderson@gmail.com"
u3.username = "dum"
u3.set_password("ilovejenn")
u3.city = "Provo"
u3.state = "UT"
u3.phone = 3526542156
u3.graduationDate = "2018-12-25 14:30:59"
u3.save()

d3 = Donation()
d3.give_back = "duh"
d3.my_choice = "my choice is my favorite"
d3.user = u3
d3.save()

i3 = Internship()
i3.company = c1
i3.user = u3
i3.how_obtained = "I'm just the best.  Duh!"
i3.hours_looking = 1

f31 = FullTime()
f31.company = c3
f31.user = u3
f31.date_accepted = "2016-2-25 14:30:59"
f31.expected_salary = 493000.00
f31.position_title = "Data Science"
f31.contact = y
f31.ft_hours_looking = 5
f31.salary = 504500.00
f31.position_description = "Wildlife and tech stuff"
f31.current_job = True
f31.start_date = "2016-5-25 14:30:59"
f31.avg_hours_week = 35
f31.satisfaction = VS
f31.projected_raise_time_months = 2
f31.family_friendly = True
f31.family_friendly_response = "They let my kids come to work with me"
f31.pros = "Understanding and flexible with time"
f31.cons = "Long Commute"

f32 = FullTime()
f32.company = c2
f32.user = u3
f32.date_accepted = "2013-6-25 14:30:59"
f32.expected_salary = 670000.00
f32.position_title = "Project"
f32.contact = n
f32.ft_hours_looking = 6
f32.salary = 65123.00
f32.position_description = "Assure Quality in the engineering department"
f32.current_job = False
f32.start_date = "2013-7-25 14:30:59"
f32.end_date = "2013-5-25 14:30:59"
f32.avg_hours_week = 46
f32.satisfaction = D
f32.projected_raise_time_months = 12
f32.family_friendly = True
f32.family_friendly_response = "They are very accomadating"
f32.pros = "Family Friendly, good music"
f32.cons = "Bad temperature control"

f33 = FullTime()
f33.company = c1
f33.user = u3
f33.date_accepted = "2014-6-25 14:30:59"
f33.expected_salary = 670000.00
f33.position_title = "Mobile/Web Dev"
f33.contact = y
f33.ft_hours_looking = 15
f33.salary = 670600.00
f33.position_description = "Assure Quality in the engineering department"
f33.current_job = False
f33.start_date = "2014-7-25 14:30:59"
f33.end_date = "2015-5-25 14:30:59"
f33.avg_hours_week = 43
f33.satisfaction = S
f33.projected_raise_time_months = 4
f33.family_friendly = True
f33.family_friendly_response = "They are very accomadating"
f33.pros = "Family Friendly, good music"
f33.cons = "Bad water"


s7 = Skills()
s7.full_time = f31
s7.skill = 'IS'

s8 = Skills()
s8.full_time = f31
s8.skill = 'GA'

s9 = Skills()
s9.full_time = f32
s9.skill = 'CFS'

s10 = Skills()
s10.full_time = f33
s10.skill = 'WB'

s11 = Skills()
s11.full_time = f33
s11.skill = 'PP'

es2 = ExitSurvey()
es2.user = u2
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
es2.ca_appointment = 6
es2.ca_help_rating = 8
es2.ca_suggestions = "Very good"
#academic advisor response
es2.academic_advisor = aa1
es2.aa_appointment = 6
es2.aa_help_rating = 7
es2.aa_suggestions = "So helpful"
