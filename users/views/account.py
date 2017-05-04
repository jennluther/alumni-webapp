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
@permission_required('users.change_user', login_url='/users/login/')
def process_request(request):
    #pull all products from the DB
    if request.user.alumni == True:
        try:
            alumni = umod.User.objects.get(id=request.user.id)
            #products = cmod.Product.objects.get(id=request.GET.get('id'))
        except umod.User.DoesNotExist:
            return HttpResponseRedirect('/homepage/index')

        try:
            exitSurvey = umod.ExitSurvey.objects.get(user = alumni.id)
        except umod.ExitSurvey.DoesNotExist:
            exitSurvey = False

        try:
            pastFullTime = umod.FullTime.objects.filter(user = alumni.id, current_job = False)
            if not pastFullTime:
                pastFullTime = False
            print(pastFullTime)
        except umod.FullTime.DoesNotExist:
            pastFullTime = False

        try:
            currentFullTime = umod.FullTime.objects.get(user = alumni.id, current_job = True)
        except umod.FullTime.DoesNotExist:
            currentFullTime = False

        try:
            internship = umod.Internship.objects.filter(user = alumni.id)
            if not internship:
                internship = False
        except umod.Internship.DoesNotExist:
            internship = False

        try:
            offer = umod.Offers.objects.filter(user = alumni.id)
            if not offer:
                offer = False
        except umod.Offers.DoesNotExist:
            offer = False

        current_skills_list = None

        if currentFullTime != False:
            skills_current_ft = umod.Skills.objects.filter(full_time = currentFullTime.id)
            for s in skills_current_ft:
                if current_skills_list is None:
                    current_skills_list = s.skill
                else:
                    current_skills_list = current_skills_list + '; ' + s.skill

        qry = umod.FullTime.objects.filter(user = alumni.id, current_job = False)
        past_full_time = []
        for q in qry:
            obj = []
            obj.append(q.id)
            obj.append('Company: ' + q.company.name)
            obj.append('Position: ' + q.position_title)
            skills = umod.Skills.objects.filter(full_time = q.id)
            skills_string = None
            for s in skills:
                if skills_string is None:
                    skills_string = s.skill
                else:
                    skills_string = skills_string + '; ' + s.skill
            obj.append('Skills: ' + str(skills_string))
            obj.append('Start Date: ' + str(q.start_date))
            obj.append('Salary: ' + str(q.salary))
            obj.append('Average Work Week (hours): ' + str(q.avg_hours_week))
            obj.append('Satisfaction: ' + q.satisfaction)
            obj.append('Projected Raise Time (months): ' + str(q.projected_raise_time_months))
            if q.family_friendly == True:
                obj.append('Family Friendly: Yes')
            else:
                obj.append('Family Friendly: No')
            obj.append('Why: ' + q.family_friendly_response)
            obj.append('Pros: ' + q.pros)
            obj.append('Cons: ' + q.cons)
            past_full_time.append(obj)

        table = QuotesTable()
        for p in past_full_time:
            table.append(p)

        #render the template
        context = {
            'alumni': alumni,
            'exitSurvey': exitSurvey,
            'pastFullTime': pastFullTime,
            'currentFullTime': currentFullTime,
            'internship': internship,
            'current_skills_list': current_skills_list,
            'table': table,
            'offer': offer,
            # 'skill_past_ft': skill_past_ft,
        }
        return dmp_render(request, 'account.html', context)
    else:
        return dmp_render(request, 'account.html')


class QuotesTable(list):
    '''
    A simple class to create an HTML table.
    This inherits from list, so add to it just as you would any other list in python:
        qry = hmod.Quote.objects.....()
        table = QuotesTable()
        table.append([ 'Cell 1a', 'Cell 1b', 'Cell 1c' ])
        table.append([ 'Cell 2a', 'Cell 2b', 'Cell 2c' ])
        print(table)
    '''
    table_id = 'quotes_table'
    def __str__(self):
        '''
        Prints the html for the table.
        '''
        # start the table
        html = []
        for row_i, row in enumerate(self):
            html.append('<div class="leftindent">')
            html.append('<h4>{}'.format(row[1]) + '  <a href="/users/currentjob/{}"><button class="btn btn-info btn-sm">Update</button></a>'.format(row[0]) + '  <a href="/users/currentjob.delete/{}/"><button class="delete_job btn btn-danger btn-sm">Delete</button></a></h4>'.format(row[0]))
            html.append('<div class="doubleleftindent">')
            for val in row[2:]:
                html.append('<p>{}</p>'.format(val))
            html.append('</div>')
            html.append('</div><hr>')
        return '\n'.join(html)



###################
### Update MyAccount
@view_function
@permission_required('users.change_user', login_url='/users/login/')
def update(request):

    form = MyAccountForm(request, initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'username': request.user.username,
        'email': request.user.email,
        'phone': request.user.phone,
        'city': request.user.city,
        'state': request.user.state,
        'street': request.user.street,
        'country': request.user.country,
        'zipcode': request.user.zipcode,
    })
    if form.is_valid():
        print('>>> form is valid')
        form.commit()
        print("/././././././ Commit completed")
        return HttpResponseRedirect('/users/account/')

    #render the template
    context = {
        # 'user': user,
        'form': form,

    }
    return dmp_render(request, 'account.update.html', context)

class MyAccountForm(FormMixIn, forms.Form):

    def init(self):
        self.fields['first_name'] = forms.CharField(label='First Name', max_length=100)
        self.fields['last_name'] = forms.CharField(label='Last Name', max_length=100)
        self.fields['username'] = forms.CharField(label='User Name', max_length=100)
        self.fields['email'] = forms.EmailField(label='Email')
        self.fields['phone'] = forms.CharField(label='Phone', max_length=30)
        self.fields['street'] = forms.CharField(label='Street', max_length=150)
        self.fields['city'] = forms.CharField(label='City', max_length=30)
        self.fields['state'] = forms.CharField(label='State', max_length=30)
        self.fields['country'] = forms.CharField(label='Country', max_length=150)
        self.fields['zipcode'] = forms.CharField(label='Zip Code', max_length=30)

    def clean_username(self):
       username = self.cleaned_data.get('username')
       if umod.User.objects.filter(username=username).exclude(id=self.request.user.id):
           raise forms.ValidationError('Username is already in use.')
       return username

    def commit(self):
        print("============ IN COMMIT")
        self.request.user.first_name = self.cleaned_data.get('first_name')
        self.request.user.last_name = self.cleaned_data.get('last_name')
        self.request.user.username = self.cleaned_data.get('username')
        self.request.user.email = self.cleaned_data.get('email')
        self.request.user.phone = self.cleaned_data.get('phone')
        self.request.user.street = self.cleaned_data.get('street')
        self.request.user.city = self.cleaned_data.get('city')
        self.request.user.state = self.cleaned_data.get('state')
        self.request.user.country = self.cleaned_data.get('country')
        self.request.user.zipcode = self.cleaned_data.get('zipcode')
        self.request.user.save()
