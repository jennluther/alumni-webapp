# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493407251.805375
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
        def content():
            return render_content(context._locals(__M_locals))
        internship = context.get('internship', UNDEFINED)
        table = context.get('table', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        user = context.get('user', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
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
        def content():
            return render_content(context)
        internship = context.get('internship', UNDEFINED)
        table = context.get('table', UNDEFINED)
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        user = context.get('user', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
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
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/aluminfo.html", "uri": "aluminfo.html", "line_map": {"128": 62, "129": 67, "130": 69, "136": 130, "29": 0, "43": 1, "48": 76, "54": 4, "67": 4, "68": 6, "69": 6, "70": 9, "71": 10, "72": 10, "73": 10, "74": 11, "75": 12, "76": 14, "77": 17, "78": 17, "79": 19, "80": 20, "81": 22, "82": 22, "83": 24, "84": 24, "85": 26, "86": 26, "87": 27, "88": 27, "89": 28, "90": 28, "91": 29, "92": 29, "93": 30, "94": 30, "95": 31, "96": 31, "97": 32, "98": 32, "99": 33, "100": 33, "101": 34, "102": 34, "103": 35, "104": 35, "105": 36, "106": 36, "107": 41, "108": 42, "109": 43, "110": 45, "111": 45, "112": 48, "113": 52, "114": 52, "115": 53, "116": 54, "117": 56, "118": 57, "119": 58, "120": 58, "121": 58, "122": 58, "123": 60, "124": 60, "125": 61, "126": 61, "127": 62}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
