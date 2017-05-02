# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493741596.034944
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
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        user = context.get('user', UNDEFINED)
        offer = context.get('offer', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        table = context.get('table', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
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
        current_skills_list = context.get('current_skills_list', UNDEFINED)
        user = context.get('user', UNDEFINED)
        offer = context.get('offer', UNDEFINED)
        internship = context.get('internship', UNDEFINED)
        table = context.get('table', UNDEFINED)
        pastFullTime = context.get('pastFullTime', UNDEFINED)
        exitSurvey = context.get('exitSurvey', UNDEFINED)
        currentFullTime = context.get('currentFullTime', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n  <h1>')
        __M_writer(str( user.first_name + " " + user.last_name))
        __M_writer("'s Information:</h1>\r\n\r\n  <div>\r\n")
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
{"line_map": {"29": 0, "44": 1, "49": 169, "55": 4, "69": 4, "70": 6, "71": 6, "72": 9, "73": 10, "74": 10, "75": 10, "76": 11, "77": 12, "78": 12, "79": 12, "80": 14, "81": 17, "82": 17, "83": 19, "84": 20, "85": 22, "86": 22, "87": 24, "88": 24, "89": 26, "90": 26, "91": 27, "92": 27, "93": 28, "94": 28, "95": 29, "96": 29, "97": 30, "98": 30, "99": 31, "100": 31, "101": 32, "102": 32, "103": 33, "104": 33, "105": 34, "106": 34, "107": 35, "108": 35, "109": 36, "110": 36, "111": 41, "112": 42, "113": 43, "114": 45, "115": 45, "116": 48, "117": 53, "118": 53, "119": 54, "120": 55, "121": 57, "122": 58, "123": 59, "124": 59, "125": 60, "126": 60, "127": 61, "128": 61, "129": 64, "130": 64, "131": 65, "132": 65, "133": 66, "134": 66, "135": 71, "136": 73, "137": 76, "138": 76, "139": 77, "140": 78, "141": 80, "142": 81, "143": 82, "144": 82, "145": 83, "146": 83, "147": 84, "148": 84, "149": 87, "150": 87, "151": 92, "152": 94, "158": 152}, "uri": "aluminfo.html", "filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/aluminfo.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
