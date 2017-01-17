# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484693123.9589875
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/account_info.html'
_template_uri = 'account_info.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<form action="/contact-info/" method="post">\r\n  <h1>Contact Information</h1>\r\n    <label for="first_name">First name: </label><br>\r\n    <input id="first_name" type="text" name="first_name" value="{{ current_fname }}"><br><br>\r\n    <label for="last_name">Last name: </label><br>\r\n    <input id="last_name" type="text" name="last_name" value="{{ current_lname }}"><br><br>\r\n    <label for="email">Email: </label><br>\r\n    <input id="email" type="text" name="email" value="{{ current_email }}"><br><br>\r\n    <label for="phone">Phone number: </label><br>\r\n    <input id="phone" type="text" name="phone" value="{{ current_phone }}"><br><br>\r\n\r\n  <h1>Job Information</h1>\r\n    <label for="company">Company: </label><br>\r\n    <input id="company" type="text" name="company" value="{{ current_company }}"><br><br>\r\n    <label for="salary">Salary: </label><br>\r\n    <input id="salary" type="text" name="salary" value="{{ current_salary }}"><br><br><br>\r\n\r\n    <input type="submit" value="Save">\r\n</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"17": 0, "28": 22, "22": 1}, "uri": "account_info.html", "source_encoding": "utf-8", "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/account_info.html"}
__M_END_METADATA
"""
