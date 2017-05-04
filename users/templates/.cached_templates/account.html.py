# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493931978.083908
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/account.html'
_template_uri = 'account.html'
_source_encoding = 'utf-8'
import django_mako_plus
import os, os.path, re, json
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        table = context.get('table', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        alumni = context.get('alumni', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        request = context.get('request', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        offer = context.get('offer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        table = context.get('table', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        def content():
            return render_content(context)
        alumni = context.get('alumni', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        request = context.get('request', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        offer = context.get('offer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container ">\r\n')
        if request.user.last_name.endswith('s'):
            __M_writer('    <h1>')
            __M_writer(str( request.user.first_name + " " + request.user.last_name))
            __M_writer("' Information:</h1>\r\n")
        else:
            __M_writer('    <h1>')
            __M_writer(str( request.user.first_name + " " + request.user.last_name))
            __M_writer("'s Information:</h1>\r\n")
        __M_writer("  <p class='box' id='account'>\r\n      <strong>Username:</strong> ")
        __M_writer(str( request.user.username ))
        __M_writer(' <br>\r\n      <strong>Phone number:</strong> ')
        __M_writer(str( request.user.phone ))
        __M_writer(' <br>\r\n      <strong>Email:</strong> ')
        __M_writer(str( request.user.email ))
        __M_writer('<br>\r\n      <strong>Address:</strong> ')
        __M_writer(str( request.user.street ))
        __M_writer('\r\n      ')
        __M_writer(str( request.user.city ))
        __M_writer(',\r\n      ')
        __M_writer(str( request.user.state ))
        __M_writer('\r\n      ')
        __M_writer(str( request.user.country ))
        __M_writer('\r\n      ')
        __M_writer(str( request.user.zipcode ))
        __M_writer('\r\n')
        if request.user.alumni == True:
            __M_writer('        Program: ')
            __M_writer(str( alumni.program ))
            __M_writer('<br>\r\n        Graduation Date: ')
            __M_writer(str( alumni.graduation_semester ))
            __M_writer(' ')
            __M_writer(str( alumni.graduation_year ))
            __M_writer('\r\n')
        __M_writer('      <br><br>\r\n        <a href="/users/account.update/" class="btn btn-danger">Update</button></a>\r\n        <a href="/users/changepassword/" class="btn btn-warning">Change Password</button></a>\r\n    </p>\r\n  </div>\r\n\r\n')
        if request.user.alumni == True:
            if exitSurvey == False:
                __M_writer('    <div>\r\n        <h3>Exit Survey needs to be taken  <a href="/surveys/exit_survey/')
                __M_writer(str( alumni.id ))
                __M_writer('"<button class="btn btn-warning">Take Survey</button></a></h3>\r\n    </div>\r\n')
            __M_writer('<div>\r\n  <div class=\'job_info\'>\r\n    <a href="/surveys/choose_company/')
            __M_writer(str( alumni.id ))
            __M_writer('"><button class="btn btn-success">Add Job Information</button></a></h3>\r\n\r\n')
            if currentFullTime != False:
                __M_writer('      <div class="container currentFullTimeInfo">\r\n        <h3><strong>Current Job:</strong>\r\n           <a href="/users/currentjob/')
                __M_writer(str( currentFullTime.id))
                __M_writer('"><button class="btn btn-info">Update</button></a></h3>\r\n        <div class="leftindent">\r\n          <h4>Company: ')
                __M_writer(str( currentFullTime.company.name ))
                __M_writer('</h4>\r\n          <div class="doubleleftindent">\r\n            <p>Position: ')
                __M_writer(str( currentFullTime.position_title ))
                __M_writer('</p>\r\n            <p>Skills: ')
                __M_writer(str( current_skills_list ))
                __M_writer('</p>\r\n            <p>Start Date: ')
                __M_writer(str( currentFullTime.start_date ))
                __M_writer('</p>\r\n            <p>Salary: ')
                __M_writer(str( currentFullTime.salary ))
                __M_writer('</p>\r\n            <p>Average Work Week: ')
                __M_writer(str( currentFullTime.avg_hours_week ))
                __M_writer('</p>\r\n            <p>Satisfaction: ')
                __M_writer(str( currentFullTime.satisfaction ))
                __M_writer('</p>\r\n            <p>Projected Raise Time (months): ')
                __M_writer(str( currentFullTime.projected_raise_time_months ))
                __M_writer('</p>\r\n            <p>Family Friendly: ')
                __M_writer(str( currentFullTime.family_friendly ))
                __M_writer('</p>\r\n            <p>Why: ')
                __M_writer(str( currentFullTime.family_friendly_response ))
                __M_writer('</p>\r\n            <p>Pros: ')
                __M_writer(str( currentFullTime.pros ))
                __M_writer('</p>\r\n            <p>Cons: ')
                __M_writer(str( currentFullTime.cons ))
                __M_writer('</p>\r\n          </div>\r\n        </div>\r\n      </div>\r\n')
            __M_writer('\r\n')
            if pastFullTime != False:
                __M_writer('      <div class="container pastFullTimeInfo">\r\n        <h3><strong>Job History:</strong></h3>\r\n            ')
                __M_writer(str( table ))
                __M_writer('\r\n      </div>\r\n')
            __M_writer('    </div>\r\n\r\n\r\n    <div class=\'intern_info\'>\r\n      <div class=\'internship\'>\r\n        <a href="/surveys/choose_company/')
            __M_writer(str( alumni.id ))
            __M_writer('/internship"><button class="btn btn-success">Add Internship Information</button></a></h3>\r\n')
            if internship != False:
                __M_writer('          <div class="container currentFullTimeInfo">\r\n            <h3><strong>Internship:</strong></h3>\r\n')
                for i in internship:
                    __M_writer('                <div class="leftindent">\r\n                  <h4>Company: ')
                    __M_writer(str( i.company.name ))
                    __M_writer('\r\n                    <a href="/users/internship/')
                    __M_writer(str( i.id))
                    __M_writer('"><button class="btn btn-info btn-sm">Update</button></a>\r\n                    <a href="/users/internship.delete/')
                    __M_writer(str( i.id ))
                    __M_writer('/"><button class="delete_internship btn btn-danger btn-sm">Delete</button></a>\r\n                  </h4>\r\n                    <div class="doubleleftindent">\r\n                      <p>Position: ')
                    __M_writer(str( i.position_title ))
                    __M_writer('</p>\r\n                      <p>How the internship was obtained: ')
                    __M_writer(str( i.how_obtained ))
                    __M_writer('</p>\r\n                      <p>How many hours spent looking for internship: ')
                    __M_writer(str( i.hours_looking ))
                    __M_writer('</p>\r\n                    </div>\r\n                  </div>\r\n                <hr>\r\n')
                __M_writer('          </div>\r\n')
            __M_writer('      </div>\r\n\r\n      <div class=\'offers\'>\r\n        <a href="/surveys/choose_company/')
            __M_writer(str( alumni.id ))
            __M_writer('/offer"><button class="btn btn-success">Add Offer Information</button></a></h3>\r\n')
            if offer != False:
                __M_writer('          <div class="container currentFullTimeInfo">\r\n            <h3><strong>Offer:</strong></h3>\r\n')
                for o in offer:
                    __M_writer('                <div class="leftindent">\r\n                  <h4>Company: ')
                    __M_writer(str( o.company.name ))
                    __M_writer('\r\n                    <a href="/users/offer/')
                    __M_writer(str( o.id))
                    __M_writer('"><button class="btn btn-info btn-sm">Update</button></a>\r\n                    <a href="/users/offer.delete/')
                    __M_writer(str( o.id ))
                    __M_writer('/"><button class="delete_offer btn btn-danger btn-sm">Delete</button></a>\r\n                  </h4>\r\n                    <div class="doubleleftindent">\r\n                      <p>Offer received because of Internship: ')
                    __M_writer(str( o.intern_offer ))
                    __M_writer('</p>\r\n                    </div>\r\n                  </div>\r\n                <hr>\r\n')
                __M_writer('          </div>\r\n')
            __M_writer('      </div>\r\n\r\n    </div>\r\n  </div>\r\n</div>\r\n\r\n<!-- Delete Internship Modal -->\r\n<div class="modal fade" id="deleteInternship" role="dialog">\r\n  <div class="modal-dialog">\r\n\r\n    <!-- Modal content-->\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n        <h4 class="modal-title">Confirm</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        <p>Are you sure you want to delete this internship?  This cannot be undone.</p>\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n      </div>\r\n    </div>\r\n\r\n  </div>\r\n</div>\r\n\r\n<!-- Delete Offer Modal -->\r\n<div class="modal fade" id="deleteOffer" role="dialog">\r\n  <div class="modal-dialog">\r\n\r\n    <!-- Modal content-->\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n        <h4 class="modal-title">Confirm</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        <p>Are you sure you want to delete this offer?  This cannot be undone.</p>\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n      </div>\r\n    </div>\r\n\r\n  </div>\r\n</div>\r\n\r\n<!-- Delete Job Modal -->\r\n<div class="modal fade" id="deleteJob" role="dialog">\r\n  <div class="modal-dialog">\r\n\r\n    <!-- Modal content-->\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n        <h4 class="modal-title">Confirm</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        <p>Are you sure you want to delete this job?  This cannot be undone.</p>\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n      </div>\r\n    </div>\r\n\r\n  </div>\r\n</div>\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/account.html", "uri": "account.html", "source_encoding": "utf-8", "line_map": {"29": 0, "45": 1, "50": 189, "56": 4, "71": 4, "72": 6, "73": 7, "74": 7, "75": 7, "76": 8, "77": 9, "78": 9, "79": 9, "80": 11, "81": 12, "82": 12, "83": 13, "84": 13, "85": 14, "86": 14, "87": 15, "88": 15, "89": 16, "90": 16, "91": 17, "92": 17, "93": 18, "94": 18, "95": 19, "96": 19, "97": 20, "98": 21, "99": 21, "100": 21, "101": 22, "102": 22, "103": 22, "104": 22, "105": 24, "106": 30, "107": 31, "108": 32, "109": 33, "110": 33, "111": 36, "112": 38, "113": 38, "114": 40, "115": 41, "116": 43, "117": 43, "118": 45, "119": 45, "120": 47, "121": 47, "122": 48, "123": 48, "124": 49, "125": 49, "126": 50, "127": 50, "128": 51, "129": 51, "130": 52, "131": 52, "132": 53, "133": 53, "134": 54, "135": 54, "136": 55, "137": 55, "138": 56, "139": 56, "140": 57, "141": 57, "142": 62, "143": 63, "144": 64, "145": 66, "146": 66, "147": 69, "148": 74, "149": 74, "150": 75, "151": 76, "152": 78, "153": 79, "154": 80, "155": 80, "156": 81, "157": 81, "158": 82, "159": 82, "160": 85, "161": 85, "162": 86, "163": 86, "164": 87, "165": 87, "166": 92, "167": 94, "168": 97, "169": 97, "170": 98, "171": 99, "172": 101, "173": 102, "174": 103, "175": 103, "176": 104, "177": 104, "178": 105, "179": 105, "180": 108, "181": 108, "182": 113, "183": 115, "184": 188, "190": 184}}
__M_END_METADATA
"""
