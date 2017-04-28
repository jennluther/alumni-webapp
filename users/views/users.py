from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from users import models as umod
from django.contrib.auth.decorators import permission_required


@view_function
def process_request(request):
    #pull all users from the DB
    exitsurvey = []
    for e in umod.ExitSurvey.objects.all():
        exitsurvey.append(e.user.id)
        print("$$$$$$", e.user.id)

    if request.urlparams[0] == 'completed':
        users = umod.User.objects.filter(id__in=exitsurvey)
    elif request.urlparams[0] == "incomplete":
        users = umod.User.objects.exclude(id__in=exitsurvey)
    else:
        users = umod.User.objects.order_by('last_name').all()

    print('>>>', users)
    for u in users:
        print('>>>', u.first_name)




    #render the template
    context = {
        'users': users,

    }
    return dmp_render(request, 'users.html', context)
