# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492548905.318369
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/results.html'
_template_uri = 'results.html'
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
        exit_survey = context.get('exit_survey', UNDEFINED)
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
        exit_survey = context.get('exit_survey', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="viewcontainter container">\r\n  <h3>')
        __M_writer(str( user.first_name + " " + user.last_name + "'s" ))
        __M_writer(" Exit Survey</h3>\r\n\r\n  <div class='container'>\r\n    <p>How were you introduced to the program?  ")
        __M_writer(str( exit_survey.program_introduction ))
        __M_writer('</p>\r\n    <p>What made you decide to do the MISM? ')
        __M_writer(str( exit_survey.mism_decision ))
        __M_writer('</p>\r\n    <p>Would you do the MISM again? ')
        __M_writer(str( exit_survey.again ))
        __M_writer('</p>\r\n    <p>Why? ')
        __M_writer(str( exit_survey.again_response ))
        __M_writer('</p>\r\n    <p>What additional classes would you find helpful that were not offered?  ')
        __M_writer(str( exit_survey.additional_classes ))
        __M_writer('</p>\r\n    <p>What was the most valuable class?  ')
        __M_writer(str( exit_survey.valuable_class ))
        __M_writer('</p>\r\n    <p>Why?  ')
        __M_writer(str( exit_survey.valuable_class_response ))
        __M_writer('</p>\r\n    <p>What did you like best about the MISM and why: ')
        __M_writer(str( exit_survey.best_response ))
        __M_writer('</p>\r\n    <p>What recommendations would you have for the MISM?  ')
        __M_writer(str( exit_survey.recommendation ))
        __M_writer('</p>\r\n    <p>Date survey was taken: ')
        __M_writer(str( exit_survey.response_date ))
        __M_writer('</p>\r\n    <p>Any additional comments: ')
        __M_writer(str( exit_survey.additional_comments ))
        __M_writer("</p>\r\n  </div>\r\n\r\n  <div class='container'>\r\n    <h4>Academic Advisor</h4>\r\n    <p>Name: ")
        __M_writer(str( exit_survey.academic_advisor.aa_first_name + " " + exit_survey.academic_advisor.aa_last_name ))
        __M_writer('</p>\r\n    <p>Number of Appointments: ')
        __M_writer(str( exit_survey.aa_appointment ))
        __M_writer('</p>\r\n    <p>Advisor help rating: ')
        __M_writer(str( exit_survey.aa_help_rating ))
        __M_writer('</p>\r\n    <p>Advisor suggestions: ')
        __M_writer(str( exit_survey.aa_suggestions ))
        __M_writer("</p>\r\n  </div>\r\n\r\n  <div class='container'>\r\n    <h4>Career Advisor</h4>\r\n    <p>Name: ")
        __M_writer(str( exit_survey.career_advisor.ca_first_name + " " + exit_survey.career_advisor.ca_last_name ))
        __M_writer('</p>\r\n    <p>Number of Appointments: ')
        __M_writer(str( exit_survey.ca_appointment ))
        __M_writer('</p>\r\n    <p>Advisor help rating: ')
        __M_writer(str( exit_survey.ca_help_rating ))
        __M_writer('</p>\r\n    <p>Advisor suggestions: ')
        __M_writer(str( exit_survey.ca_suggestions ))
        __M_writer('</p>\r\n  </div>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/results.html", "uri": "results.html", "line_map": {"29": 0, "38": 1, "43": 39, "49": 4, "57": 4, "58": 6, "59": 6, "60": 9, "61": 9, "62": 10, "63": 10, "64": 11, "65": 11, "66": 12, "67": 12, "68": 13, "69": 13, "70": 14, "71": 14, "72": 15, "73": 15, "74": 16, "75": 16, "76": 17, "77": 17, "78": 18, "79": 18, "80": 19, "81": 19, "82": 24, "83": 24, "84": 25, "85": 25, "86": 26, "87": 26, "88": 27, "89": 27, "90": 32, "91": 32, "92": 33, "93": 33, "94": 34, "95": 34, "96": 35, "97": 35, "103": 97}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
