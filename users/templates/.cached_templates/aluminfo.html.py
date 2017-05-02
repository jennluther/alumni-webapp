# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493765262.484588
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
        user = context.get('user', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        table = context.get('table', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        offer = context.get('offer', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        user = context.get('user', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        table = context.get('table', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        offer = context.get('offer', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n  <h1>')
        __M_writer(str( user.first_name + " " + user.last_name))
        __M_writer("'s Information:</h1>\r\n  <p class='aluminfo'>\r\n      Phone number: ")
        __M_writer(str( user.phone ))
        __M_writer(' <br>\r\n      Email: ')
        __M_writer(str( user.email ))
        __M_writer('<br>\r\n      Address: ')
        __M_writer(str( user.street ))
        __M_writer('\r\n      ')
        __M_writer(str( user.city ))
        __M_writer(',\r\n      ')
        __M_writer(str( user.state ))
        __M_writer('\r\n      ')
        __M_writer(str( user.country ))
        __M_writer('\r\n      ')
        __M_writer(str( user.zipcode ))
        __M_writer('<br>\r\n      Program: ')
        __M_writer(str( user.program ))
        __M_writer('<br>\r\n      Graduation Date: ')
        __M_writer(str( user.graduationDate ))
        __M_writer('<br>\r\n      <a href="/users/user/')
        __M_writer(str( user.id ))
        __M_writer('/">Edit</a>\r\n    </p>\r\n  <div>\r\n')
        if exitSurvey != False:
            __M_writer('      <h3>Exit Survey has been submitted!  <a href="/users/results/')
            __M_writer(str( user.id ))
            __M_writer('"<button class="btn btn-warning">Results</button></a><h3>\r\n')
        else:
            __M_writer('      <h3>Exit Survey needs to be taken  <a href="/surveys/exit_survey/')
            __M_writer(str( user.id ))
            __M_writer('"<button class="btn btn-warning">Take Survey</button></a></h3>\r\n')
        __M_writer('  </div>\r\n<div>\r\n  <div class=\'job_info\'>\r\n    <a href="/surveys/choose_company/')
        __M_writer(str( user.id ))
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
        __M_writer(str( user.id ))
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
        __M_writer(str( user.id ))
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
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/aluminfo.html", "uri": "aluminfo.html", "line_map": {"29": 0, "44": 1, "49": 180, "55": 4, "69": 4, "70": 6, "71": 6, "72": 8, "73": 8, "74": 9, "75": 9, "76": 10, "77": 10, "78": 11, "79": 11, "80": 12, "81": 12, "82": 13, "83": 13, "84": 14, "85": 14, "86": 15, "87": 15, "88": 16, "89": 16, "90": 17, "91": 17, "92": 20, "93": 21, "94": 21, "95": 21, "96": 22, "97": 23, "98": 23, "99": 23, "100": 25, "101": 28, "102": 28, "103": 30, "104": 31, "105": 33, "106": 33, "107": 35, "108": 35, "109": 37, "110": 37, "111": 38, "112": 38, "113": 39, "114": 39, "115": 40, "116": 40, "117": 41, "118": 41, "119": 42, "120": 42, "121": 43, "122": 43, "123": 44, "124": 44, "125": 45, "126": 45, "127": 46, "128": 46, "129": 47, "130": 47, "131": 52, "132": 53, "133": 54, "134": 56, "135": 56, "136": 59, "137": 64, "138": 64, "139": 65, "140": 66, "141": 68, "142": 69, "143": 70, "144": 70, "145": 71, "146": 71, "147": 72, "148": 72, "149": 75, "150": 75, "151": 76, "152": 76, "153": 77, "154": 77, "155": 82, "156": 84, "157": 87, "158": 87, "159": 88, "160": 89, "161": 91, "162": 92, "163": 93, "164": 93, "165": 94, "166": 94, "167": 95, "168": 95, "169": 98, "170": 98, "171": 103, "172": 105, "178": 172}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
