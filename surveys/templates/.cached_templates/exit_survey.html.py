# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484694183.239391
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/exit_survey.html'
_template_uri = 'exit_survey.html'
_source_encoding = 'utf-8'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        TIME_RANGE = context.get('TIME_RANGE', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        TIME_RANGE = context.get('TIME_RANGE', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<form action="/contact-info/" method="post">\r\n  <h1>Job Information</h1>\r\n    <label for="offers_received">How many full-time offers did you receive? </label><br> <!--drop down of numbers-->\r\n    <input id="offers_received" type="text" name="offers_received" value="{{ current_offers_received }}"><br><br>\r\n    <label for="company">Which company did you accept an offer with? </label><br><!--make this field give suggested companies that are already in Database-->\r\n    <input id="company" type="text" name="company" value="{{ current_company }}"><br><br>\r\n    <label for="expected_salary">What is your expected salary? </label><br>\r\n    <input id="expected_salary" type="text" name="exptected_salary" value="{{ current_expected_salary }}"><br><br>\r\n    <label for="position_title">What is your position title? </label><br>\r\n    <input id="position_title" type="text" name="position_title" value="{{ current_position_title }}"><br><br>\r\n    <label for="position_description">Which of the following best describes your position? </label><br> <!--list of possible job descriptions-->\r\n    <input id="position_description" type="text" name="position_description" value="{{ current_position_description }}"><br><br>\r\n    <!--alternate position description that can take the place of the position_description-->\r\n    <!--I don\'t know if we need to do anything to allow the "other" submition to have the same tags as the position_description-->\r\n    <label for="position_description">If other, list here: </label><br> <!--list of possible job descriptions-->\r\n    <input id="position_description" type="text" name="position_description" value="{{ current_position_description }}"><br><br>\r\n\r\n    <label for="contact">Are you willing to serve as a contact for the company you\'ve selected? </label><br>\r\n    <!--pass values of y=yes, n=no and m=maybe-->\r\n    <input id="contact" type="radio" name="contact" value="y">Yes<br>\r\n    <input id="contact" type="radio" name="contact" value="n">No<br>\r\n    <input id="contact" type="radio" name="contact" value="m">Maybe<br><br>\r\n\r\n    <label for="position_description">How much time did you spend looking for your full-time position? </label><br> <!--list of possible job descriptions-->\r\n    <div class="dropdown">\r\n      <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Dropdown Example\r\n      <span class="caret"></span></button>\r\n      <ul class="dropdown-menu">\r\n')
        for item in TIME_RANGE.values():
            __M_writer('          <li>')
            __M_writer(str(item))
            __M_writer('</li>\r\n')
        __M_writer('      </ul>\r\n    </div>\r\n    <input id="position_description" type="text" name="position_description" value="{{ current_position_description }}"><br>\r\n  </form>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "exit_survey.html", "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/exit_survey.html", "line_map": {"65": 59, "36": 1, "57": 33, "54": 3, "55": 32, "56": 33, "41": 39, "58": 33, "59": 35, "28": 0, "47": 3}}
__M_END_METADATA
"""
