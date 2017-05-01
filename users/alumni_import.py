# imports for our project
from users import models as umod
from decimal import Decimal
import csv
import io

def ImportAlumni(uploaded_csv):
    print("LINE 8>>>>>>>>", uploaded_csv)
    # with open(uploaded_csv) as csvfile:
    # csvfile = io.StringIO(uploaded_csv)
    print("++++++++++++", uploaded_csv)
    reader = csv.DictReader(uploaded_csv)
    print("******************************")
    for r in reader:
        print( r )
    print("******************************")
    for row in reader:
        ######USER INFO
        u = umod.User()
        u.first_name = row['first_name']
        u.last_name = row['last_name']
        u.email = row['email']
        u.username = row['username']
        u.set_password(row['password'])
        u.city = row['city']
        u.state = row['state']
        u.phone = row['phone']
        u.graduationDate = row['graduationDate']
        u.save()
        print(u.first_name)
        ###########FULL TIME INFO
        ft = umod.FullTime()
        try:
            umod.Company.objects.get(name=row['company_name'], city=row['company_city'], state=row['company_state'])
            ft.company = umod.Company.objects.get(name=row['company_name'], city=row['company_city'], state=row['company_state'])
        except umod.Company.DoesNotExist:
            company = umod.Company()
            company.name = row['company_name']
            company.city = row['company_city']
            company.state = row['company_state']
            company.save()
            ft.company = company
        ft.user = u
        ft.date_accepted = row['ft_date_accepted']
        ft.expected_salary = row['ft_expected_salary']
        ft.position_title = row['ft_position_title']
        ft.contact = row['ft_contact']
        ft.ft_hours_looking = row['ft_hours_looking']
        ft.salary = row['ft_salary']
        ft.position_description = row['ft_position_description']
        if row['ft_current_job'] == 'TRUE':
            ft.current_job = True
        else:
            ft.current_job = False
        ft.start_date = row['ft_start_date']
        ft.end_date = row['ft_end_date']
        ft.avg_hours_week = row['ft_avg_hours_week']
        ft.satisfaction = row['ft_satisfaction']
        ft.projected_raise_time_months = row['ft_projected_raise_time_months']
        if row['ft_family_friendly'] == 'TRUE':
            ft.family_friendly = True
        else:
            ft.family_friendly = False
        ft.family_friendly_response = row['ft_family_friendly_response']
        ft.pros = row['ft_pros']
        ft.cons = row['ft_cons']
        ft.save()

        ########INTERNSHIP INFO
        # i = umod.Internship()
        # try:
        #     umod.Company.objects.get(name=row['intern_company_name'], city=row['intern_company_city'], state=row['intern_company_state'])
        #     i.company = umod.Company.objects.get(name=row['intern_company_name'], city=row['intern_company_city'], state=row['intern_company_state'])
        # except umod.Company.DoesNotExist:
        #     company = umod.Company()
        #     company.name = row['intern_company_name']
        #     company.city = row['intern_company_city']
        #     company.state = row['intern_company_state']
        #     company.save()
        #     i.company = company
        # i.user = u
        # i.how_obtained = row['intern_how_obtained']
        # i.hours_looking = row['intern_hours_looking']
        # i.position_title = row['intern_position_title']
        # i.save()
        #
        # ########OFFER INFO
        # o = umod.Offers()
        # try:
        #     umod.Company.objects.get(name=row['offer_company_name'], city=row['offer_company_city'], state=row['offer_company_state'])
        #     o.company = umod.Company.objects.get(name=row['offer_company_name'], city=row['offer_company_city'], state=row['offer_company_state'])
        # except umod.Company.DoesNotExist:
        #     company = umod.Company()
        #     company.name = row['offer_company_name']
        #     company.city = row['offer_company_city']
        #     company.state = row['offer_company_state']
        #     company.save()
        #     o.company = company
        # o.user = u
        # o.intern_offer = row['intern_offer']
