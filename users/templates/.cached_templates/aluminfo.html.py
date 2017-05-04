# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493919429.307063
_enable_loop = True
_template_filename = '/Users/Jenn/Programs/alumni-webapp/users/templates/aluminfo.html'
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
        alumni = context.get('alumni', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        offer = context.get('offer', UNDEFINED)
        table = context.get('table', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        alumni = context.get('alumni', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        def content():
            return render_content(context)
        offer = context.get('offer', UNDEFINED)
        table = context.get('table', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="container">\n  <h1>')
        __M_writer(str( alumni.first_name + " " + alumni.last_name))
        __M_writer("'s Information:</h1>\n  <p class='aluminfo'>\n      Phone number: ")
        __M_writer(str( alumni.phone ))
        __M_writer(' <br>\n      Email: ')
        __M_writer(str( alumni.email ))
        __M_writer('<br>\n      Address: ')
        __M_writer(str( alumni.street ))
        __M_writer('\n      ')
        __M_writer(str( alumni.city ))
        __M_writer(',\n      ')
        __M_writer(str( alumni.state ))
        __M_writer('\n      ')
        __M_writer(str( alumni.country ))
        __M_writer('\n      ')
        __M_writer(str( alumni.zipcode ))
        __M_writer('<br>\n      Program: ')
        __M_writer(str( alumni.program ))
        __M_writer('<br>\n      Graduation Date: ')
        __M_writer(str( alumni.graduation_semester ))
        __M_writer(' ')
        __M_writer(str( alumni.graduation_year ))
        __M_writer('<br>\n      <a href="/users/user/')
        __M_writer(str( alumni.id ))
        __M_writer('/">Edit</a>\n    </p>\n  <div>\n')
        if exitSurvey != False:
            __M_writer('      <h3>Exit Survey has been submitted!  <a href="/users/results/')
            __M_writer(str( alumni.id ))
            __M_writer('"<button class="btn btn-warning">Results</button></a><h3>\n')
        else:
            __M_writer('      <h3>Exit Survey needs to be taken  <a href="/surveys/exit_survey/')
            __M_writer(str( alumni.id ))
            __M_writer('"<button class="btn btn-warning">Take Survey</button></a></h3>\n')
        __M_writer('  </div>\n<div>\n  <div class=\'job_info\'>\n    <a href="/surveys/choose_company/')
        __M_writer(str( alumni.id ))
        __M_writer('"><button class="btn btn-success">Add Job Information</button></a></h3>\n\n')
        if currentFullTime != False:
            __M_writer('      <div class="container currentFullTimeInfo">\n        <h3><strong>Current Job:</strong>\n           <a href="/users/currentjob/')
            __M_writer(str( currentFullTime.id))
            __M_writer('"><button class="btn btn-info">Update</button></a></h3>\n        <div class="leftindent">\n          <h4>Company: ')
            __M_writer(str( currentFullTime.company.name ))
            __M_writer('</h4>\n          <div class="doubleleftindent">\n            <p>Position: ')
            __M_writer(str( currentFullTime.position_title ))
            __M_writer('</p>\n            <p>Skills: ')
            __M_writer(str( current_skills_list ))
            __M_writer('</p>\n            <p>Start Date: ')
            __M_writer(str( currentFullTime.start_date ))
            __M_writer('</p>\n            <p>Salary: ')
            __M_writer(str( currentFullTime.salary ))
            __M_writer('</p>\n            <p>Average Work Week: ')
            __M_writer(str( currentFullTime.avg_hours_week ))
            __M_writer('</p>\n            <p>Satisfaction: ')
            __M_writer(str( currentFullTime.satisfaction ))
            __M_writer('</p>\n            <p>Projected Raise Time (months): ')
            __M_writer(str( currentFullTime.projected_raise_time_months ))
            __M_writer('</p>\n            <p>Family Friendly: ')
            __M_writer(str( currentFullTime.family_friendly ))
            __M_writer('</p>\n            <p>Why: ')
            __M_writer(str( currentFullTime.family_friendly_response ))
            __M_writer('</p>\n            <p>Pros: ')
            __M_writer(str( currentFullTime.pros ))
            __M_writer('</p>\n            <p>Cons: ')
            __M_writer(str( currentFullTime.cons ))
            __M_writer('</p>\n          </div>\n        </div>\n      </div>\n')
        __M_writer('\n')
        if pastFullTime != False:
            __M_writer('      <div class="container pastFullTimeInfo">\n        <h3><strong>Job History:</strong></h3>\n            ')
            __M_writer(str( table ))
            __M_writer('\n      </div>\n')
        __M_writer('    </div>\n\n\n    <div class=\'intern_info\'>\n      <div class=\'internship\'>\n        <a href="/surveys/choose_company/')
        __M_writer(str( alumni.id ))
        __M_writer('/internship"><button class="btn btn-success">Add Internship Information</button></a></h3>\n')
        if internship != False:
            __M_writer('          <div class="container currentFullTimeInfo">\n            <h3><strong>Internship:</strong></h3>\n')
            for i in internship:
                __M_writer('                <div class="leftindent">\n                  <h4>Company: ')
                __M_writer(str( i.company.name ))
                __M_writer('\n                    <a href="/users/internship/')
                __M_writer(str( i.id))
                __M_writer('"><button class="btn btn-info btn-sm">Update</button></a>\n                    <a href="/users/internship.delete/')
                __M_writer(str( i.id ))
                __M_writer('/"><button class="delete_internship btn btn-danger btn-sm">Delete</button></a>\n                  </h4>\n                    <div class="doubleleftindent">\n                      <p>Position: ')
                __M_writer(str( i.position_title ))
                __M_writer('</p>\n                      <p>How the internship was obtained: ')
                __M_writer(str( i.how_obtained ))
                __M_writer('</p>\n                      <p>How many hours spent looking for internship: ')
                __M_writer(str( i.hours_looking ))
                __M_writer('</p>\n                    </div>\n                  </div>\n                <hr>\n')
            __M_writer('          </div>\n')
        __M_writer('      </div>\n\n      <div class=\'offers\'>\n        <a href="/surveys/choose_company/')
        __M_writer(str( alumni.id ))
        __M_writer('/offer"><button class="btn btn-success">Add Offer Information</button></a></h3>\n')
        if offer != False:
            __M_writer('          <div class="container currentFullTimeInfo">\n            <h3><strong>Offer:</strong></h3>\n')
            for o in offer:
                __M_writer('                <div class="leftindent">\n                  <h4>Company: ')
                __M_writer(str( o.company.name ))
                __M_writer('\n                    <a href="/users/offer/')
                __M_writer(str( o.id))
                __M_writer('"><button class="btn btn-info btn-sm">Update</button></a>\n                    <a href="/users/offer.delete/')
                __M_writer(str( o.id ))
                __M_writer('/"><button class="delete_offer btn btn-danger btn-sm">Delete</button></a>\n                  </h4>\n                    <div class="doubleleftindent">\n                      <p>Offer received because of Internship: ')
                __M_writer(str( o.intern_offer ))
                __M_writer('</p>\n                    </div>\n                  </div>\n                <hr>\n')
            __M_writer('          </div>\n')
        __M_writer('      </div>\n\n    </div>\n  </div>\n</div>\n\n<!-- Delete Internship Modal -->\n<div class="modal fade" id="deleteInternship" role="dialog">\n<div class="modal-dialog">\n\n  <!-- Modal content-->\n  <div class="modal-content">\n    <div class="modal-header">\n      <button type="button" class="close" data-dismiss="modal">&times;</button>\n      <h4 class="modal-title">Confirm</h4>\n    </div>\n    <div class="modal-body">\n      <p>Are you sure you want to delete this internship?  This cannot be undone.</p>\n    </div>\n    <div class="modal-footer">\n      <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\n      <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\n    </div>\n  </div>\n\n</div>\n</div>\n\n<!-- Delete Offer Modal -->\n<div class="modal fade" id="deleteOffer" role="dialog">\n<div class="modal-dialog">\n\n  <!-- Modal content-->\n  <div class="modal-content">\n    <div class="modal-header">\n      <button type="button" class="close" data-dismiss="modal">&times;</button>\n      <h4 class="modal-title">Confirm</h4>\n    </div>\n    <div class="modal-body">\n      <p>Are you sure you want to delete this offer?  This cannot be undone.</p>\n    </div>\n    <div class="modal-footer">\n      <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\n      <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\n    </div>\n  </div>\n\n</div>\n</div>\n\n<!-- Delete Job Modal -->\n<div class="modal fade" id="deleteJob" role="dialog">\n<div class="modal-dialog">\n\n  <!-- Modal content-->\n  <div class="modal-content">\n    <div class="modal-header">\n      <button type="button" class="close" data-dismiss="modal">&times;</button>\n      <h4 class="modal-title">Confirm</h4>\n    </div>\n    <div class="modal-body">\n      <p>Are you sure you want to delete this job?  This cannot be undone.</p>\n    </div>\n    <div class="modal-footer">\n      <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\n      <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\n    </div>\n  </div>\n\n</div>\n</div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jenn/Programs/alumni-webapp/users/templates/aluminfo.html", "uri": "aluminfo.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 180, "55": 4, "69": 4, "70": 6, "71": 6, "72": 8, "73": 8, "74": 9, "75": 9, "76": 10, "77": 10, "78": 11, "79": 11, "80": 12, "81": 12, "82": 13, "83": 13, "84": 14, "85": 14, "86": 15, "87": 15, "88": 16, "89": 16, "90": 16, "91": 16, "92": 17, "93": 17, "94": 20, "95": 21, "96": 21, "97": 21, "98": 22, "99": 23, "100": 23, "101": 23, "102": 25, "103": 28, "104": 28, "105": 30, "106": 31, "107": 33, "108": 33, "109": 35, "110": 35, "111": 37, "112": 37, "113": 38, "114": 38, "115": 39, "116": 39, "117": 40, "118": 40, "119": 41, "120": 41, "121": 42, "122": 42, "123": 43, "124": 43, "125": 44, "126": 44, "127": 45, "128": 45, "129": 46, "130": 46, "131": 47, "132": 47, "133": 52, "134": 53, "135": 54, "136": 56, "137": 56, "138": 59, "139": 64, "140": 64, "141": 65, "142": 66, "143": 68, "144": 69, "145": 70, "146": 70, "147": 71, "148": 71, "149": 72, "150": 72, "151": 75, "152": 75, "153": 76, "154": 76, "155": 77, "156": 77, "157": 82, "158": 84, "159": 87, "160": 87, "161": 88, "162": 89, "163": 91, "164": 92, "165": 93, "166": 93, "167": 94, "168": 94, "169": 95, "170": 95, "171": 98, "172": 98, "173": 103, "174": 105, "180": 174}}
__M_END_METADATA
"""
