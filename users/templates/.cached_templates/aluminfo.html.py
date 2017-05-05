# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493996839.563597
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/aluminfo.html'
_template_uri = 'aluminfo.html'
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
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        offer = context.get('offer', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        table = context.get('table', UNDEFINED)
        alumni = context.get('alumni', UNDEFINED)
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
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        offer = context.get('offer', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        def content():
            return render_content(context)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        table = context.get('table', UNDEFINED)
        alumni = context.get('alumni', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n')
        if alumni.last_name.endswith('s'):
            __M_writer('    <h1>')
            __M_writer(str( alumni.first_name + " " + alumni.last_name))
            __M_writer(' Information:</h1>\r\n')
        else:
            __M_writer('    <h1>')
            __M_writer(str( alumni.first_name + " " + alumni.last_name))
            __M_writer("'s Information:</h1>\r\n")
        __M_writer("  <p class='box' id='aluminfo'>\r\n      Phone Number: ")
        __M_writer(str( alumni.phone ))
        __M_writer(' <br>\r\n      Email: ')
        __M_writer(str( alumni.email ))
        __M_writer('<br>\r\n      Address: ')
        __M_writer(str( alumni.street ))
        __M_writer('\r\n      ')
        __M_writer(str( alumni.city ))
        __M_writer(',\r\n      ')
        __M_writer(str( alumni.state ))
        __M_writer('\r\n      ')
        __M_writer(str( alumni.country ))
        __M_writer('\r\n      ')
        __M_writer(str( alumni.zipcode ))
        __M_writer('<br>\r\n      Program: ')
        __M_writer(str( alumni.program ))
        __M_writer('<br>\r\n      Graduation Date: ')
        __M_writer(str( alumni.graduation_semester ))
        __M_writer(' ')
        __M_writer(str( alumni.graduation_year ))
        __M_writer('<br><br>\r\n      <a href="/users/user/')
        __M_writer(str( alumni.id ))
        __M_writer('" class="btn btn-danger">Update</button></a>\r\n      <a href="/users/activate_user/')
        __M_writer(str( alumni.id ))
        __M_writer('" class="btn btn-warning">Change Password</button></a>\r\n    </p>\r\n  <div>\r\n')
        if exitSurvey != False:
            __M_writer('      <h3>Exit Survey has been submitted!  <a href="/users/results/')
            __M_writer(str( alumni.id ))
            __M_writer('"<button class="btn btn-warning">Results</button></a><h3>\r\n')
        else:
            __M_writer('      <h3>Exit Survey needs to be taken  <a href="/surveys/exit_survey/')
            __M_writer(str( alumni.id ))
            __M_writer('"<button class="btn btn-warning">Take Survey</button></a></h3>\r\n')
        __M_writer('  </div>\r\n<div>\r\n  <div class=\'job_info\'>\r\n    <a href="/surveys/choose_company/')
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
        __M_writer('      </div>\r\n\r\n    </div>\r\n  </div>\r\n</div>\r\n\r\n<!-- Delete Internship Modal -->\r\n<div class="modal fade" id="deleteInternship" role="dialog">\r\n<div class="modal-dialog">\r\n\r\n  <!-- Modal content-->\r\n  <div class="modal-content">\r\n    <div class="modal-header">\r\n      <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n      <h4 class="modal-title">Confirm</h4>\r\n    </div>\r\n    <div class="modal-body">\r\n      <p>Are you sure you want to delete this internship?  This cannot be undone.</p>\r\n    </div>\r\n    <div class="modal-footer">\r\n      <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\r\n      <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n    </div>\r\n  </div>\r\n\r\n</div>\r\n</div>\r\n\r\n<!-- Delete Offer Modal -->\r\n<div class="modal fade" id="deleteOffer" role="dialog">\r\n<div class="modal-dialog">\r\n\r\n  <!-- Modal content-->\r\n  <div class="modal-content">\r\n    <div class="modal-header">\r\n      <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n      <h4 class="modal-title">Confirm</h4>\r\n    </div>\r\n    <div class="modal-body">\r\n      <p>Are you sure you want to delete this offer?  This cannot be undone.</p>\r\n    </div>\r\n    <div class="modal-footer">\r\n      <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\r\n      <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n    </div>\r\n  </div>\r\n\r\n</div>\r\n</div>\r\n\r\n<!-- Delete Job Modal -->\r\n<div class="modal fade" id="deleteJob" role="dialog">\r\n<div class="modal-dialog">\r\n\r\n  <!-- Modal content-->\r\n  <div class="modal-content">\r\n    <div class="modal-header">\r\n      <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n      <h4 class="modal-title">Confirm</h4>\r\n    </div>\r\n    <div class="modal-body">\r\n      <p>Are you sure you want to delete this job?  This cannot be undone.</p>\r\n    </div>\r\n    <div class="modal-footer">\r\n      <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\r\n      <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n    </div>\r\n  </div>\r\n\r\n</div>\r\n</div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/aluminfo.html", "source_encoding": "utf-8", "uri": "aluminfo.html", "line_map": {"29": 0, "44": 1, "49": 185, "55": 4, "69": 4, "70": 6, "71": 7, "72": 7, "73": 7, "74": 8, "75": 9, "76": 9, "77": 9, "78": 11, "79": 12, "80": 12, "81": 13, "82": 13, "83": 14, "84": 14, "85": 15, "86": 15, "87": 16, "88": 16, "89": 17, "90": 17, "91": 18, "92": 18, "93": 19, "94": 19, "95": 20, "96": 20, "97": 20, "98": 20, "99": 21, "100": 21, "101": 22, "102": 22, "103": 25, "104": 26, "105": 26, "106": 26, "107": 27, "108": 28, "109": 28, "110": 28, "111": 30, "112": 33, "113": 33, "114": 35, "115": 36, "116": 38, "117": 38, "118": 40, "119": 40, "120": 42, "121": 42, "122": 43, "123": 43, "124": 44, "125": 44, "126": 45, "127": 45, "128": 46, "129": 46, "130": 47, "131": 47, "132": 48, "133": 48, "134": 49, "135": 49, "136": 50, "137": 50, "138": 51, "139": 51, "140": 52, "141": 52, "142": 57, "143": 58, "144": 59, "145": 61, "146": 61, "147": 64, "148": 69, "149": 69, "150": 70, "151": 71, "152": 73, "153": 74, "154": 75, "155": 75, "156": 76, "157": 76, "158": 77, "159": 77, "160": 80, "161": 80, "162": 81, "163": 81, "164": 82, "165": 82, "166": 87, "167": 89, "168": 92, "169": 92, "170": 93, "171": 94, "172": 96, "173": 97, "174": 98, "175": 98, "176": 99, "177": 99, "178": 100, "179": 100, "180": 103, "181": 103, "182": 108, "183": 110, "189": 183}}
__M_END_METADATA
"""
