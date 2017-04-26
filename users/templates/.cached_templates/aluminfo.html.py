# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493245814.919955
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
        internship = context.get('internship', UNDEFINED)
        user = context.get('user', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
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
        internship = context.get('internship', UNDEFINED)
        user = context.get('user', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n  <h1>')
        __M_writer(str( user.first_name + " " + user.last_name))
        __M_writer("'s Information:</h1>\r\n\r\n  <div>\r\n")
        if exitSurvey != False:
            __M_writer('      <h3>Exit Survey has been submitted!  <a href="/users/results/')
            __M_writer(str( user.id ))
            __M_writer('"<button class="btn btn-warning">Results</button></a><h3>\r\n')
        else:
            __M_writer('      <h3>Exit Survey needs to be taken</h3>\r\n')
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
            __M_writer('      <div class="container pastFullTimeInfo">\r\n        <h3><strong>Job History:</strong></h3>\r\n')
            for p in pastFullTime:
                __M_writer('        <div class="leftindent">\r\n          <h4>Company: ')
                __M_writer(str( p.company.name ))
                __M_writer(' <a href="/users/currentjob/')
                __M_writer(str( p.id))
                __M_writer('"><button class="btn btn-info btn-sm">Update</button></a></h4>\r\n            <div class="doubleleftindent">\r\n            <p>Position: ')
                __M_writer(str( p.position_title ))
                __M_writer('</p>\r\n            <p>Start Date: ')
                __M_writer(str( p.start_date ))
                __M_writer('</p>\r\n            <p>End Date: ')
                __M_writer(str( p.end_date ))
                __M_writer('</p>\r\n            <p>Salary: $')
                __M_writer(str( p.salary ))
                __M_writer('</p>\r\n            <p>Average Work Week: ')
                __M_writer(str( p.avg_hours_week ))
                __M_writer('</p>\r\n            <p>Satisfaction: ')
                __M_writer(str( p.satisfaction ))
                __M_writer('</p>\r\n            <p>Projected Raise Time (months): ')
                __M_writer(str( p.projected_raise_time_months ))
                __M_writer('</p>\r\n            <p>Family Friendly: ')
                __M_writer(str( p.family_friendly ))
                __M_writer('</p>\r\n            <p>Why: ')
                __M_writer(str( p.family_friendly_response ))
                __M_writer('</p>\r\n            <p>Pros: ')
                __M_writer(str( p.pros ))
                __M_writer('</p>\r\n            <p>Cons: ')
                __M_writer(str( p.cons ))
                __M_writer('</p>\r\n          </div>\r\n        </div>\r\n          <hr>\r\n')
            __M_writer('      </div>\r\n')
        __M_writer('    </div>\r\n\r\n\r\n    <div class=\'intern_info\'>\r\n      <a href="/surveys/choose_company/')
        __M_writer(str( user.id ))
        __M_writer('/internship"><button class="btn btn-success">Add Internship Information</button></a></h3>\r\n')
        if internship != False:
            __M_writer('        <div class="container currentFullTimeInfo">\r\n          <h3><strong>Internship:</strong></h3>\r\n')
            for i in internship:
                __M_writer('              <div class="leftindent">\r\n                <h4>Company: ')
                __M_writer(str( i.company.name ))
                __M_writer(' <a href="/users/internship/')
                __M_writer(str( i.id))
                __M_writer('"><button class="btn btn-info btn-sm">Update</button></a></h4>\r\n                  <div class="doubleleftindent">\r\n                    <p>Position: ')
                __M_writer(str( i.position_title ))
                __M_writer('</p>\r\n                    <p>How the internship was obtained: ')
                __M_writer(str( i.how_obtained ))
                __M_writer('</p>\r\n                    <p>How many hours spent looking for internship: ')
                __M_writer(str( i.hours_looking ))
                __M_writer('</p>\r\n                  </div>\r\n                </div>\r\n              <hr>\r\n')
            __M_writer('        </div>\r\n')
        __M_writer('    </div>\r\n  </div>\r\n</div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/aluminfo.html", "source_encoding": "utf-8", "uri": "aluminfo.html", "line_map": {"29": 0, "41": 1, "46": 93, "52": 4, "63": 4, "64": 6, "65": 6, "66": 9, "67": 10, "68": 10, "69": 10, "70": 11, "71": 12, "72": 14, "73": 17, "74": 17, "75": 19, "76": 20, "77": 22, "78": 22, "79": 24, "80": 24, "81": 26, "82": 26, "83": 27, "84": 27, "85": 28, "86": 28, "87": 29, "88": 29, "89": 30, "90": 30, "91": 31, "92": 31, "93": 32, "94": 32, "95": 33, "96": 33, "97": 34, "98": 34, "99": 35, "100": 35, "101": 40, "102": 41, "103": 42, "104": 44, "105": 45, "106": 46, "107": 46, "108": 46, "109": 46, "110": 48, "111": 48, "112": 49, "113": 49, "114": 50, "115": 50, "116": 51, "117": 51, "118": 52, "119": 52, "120": 53, "121": 53, "122": 54, "123": 54, "124": 55, "125": 55, "126": 56, "127": 56, "128": 57, "129": 57, "130": 58, "131": 58, "132": 63, "133": 65, "134": 69, "135": 69, "136": 70, "137": 71, "138": 73, "139": 74, "140": 75, "141": 75, "142": 75, "143": 75, "144": 77, "145": 77, "146": 78, "147": 78, "148": 79, "149": 79, "150": 84, "151": 86, "157": 151}}
__M_END_METADATA
"""
