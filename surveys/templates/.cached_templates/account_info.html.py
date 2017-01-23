# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1485204932.6653914
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/account_info.html'
_template_uri = 'account_info.html'
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<form action="/contact-info/" method="post">\r\n  <h1>Contact Information</h1>\r\n  <div class="form-group">\r\n    <label for="first_name">First name: </label>\r\n    <input id="first_name" type="text" class="form-control" name="first_name" value="">\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="last_name">Last name: </label><br>\r\n    <input id="last_name" type="text" class="form-control" name="last_name" value="">\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="email">Email: </label><br>\r\n    <input id="email" type="text" class="form-control" name="email" value="">\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="phone">Phone number: </label><br>\r\n    <input id="phone" type="text" class="form-control" name="phone" value="">\r\n  </div>\r\n\r\n  <h1>Job Information</h1>\r\n  <div class="form-group">\r\n    <label for="company">Company: </label><br>\r\n    <input id="company" type="text" class="form-control" name="company" value="">\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="salary">Salary: </label><br>\r\n    <input id="salary" type="text" class="form-control" name="salary" value="">\r\n  </div>\r\n\r\n    <input type="submit" value="Save">\r\n</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "52": 3, "40": 35, "58": 52, "28": 0, "46": 3}, "uri": "account_info.html", "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/account_info.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
