# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1488578297.6337447
=======
_modified_time = 1485543001.838467
>>>>>>> 385a8df006c363b089320eba393e99870f244917
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/homepage/templates/index.html'
_template_uri = 'index.html'
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
<<<<<<< HEAD
        __M_writer('\r\n\r\n  <div class="content">\r\n    <h1>Welcome to the Information Systems Community. </h1>\r\n  </div>\r\n\r\n  <div class="home_buttons">\r\n    <a class="btn btn-success" href="#" role="button">Reports</a>\r\n    <a class="btn btn-success" href="#" role="button">Graduation Survey</a>\r\n    <a class="btn btn-success" href="#" role="button">IS News</a>\r\n  </div>\r\n\r\n')
=======
        __M_writer('\n\n  <div class="content">\n    <h1>We want your data. </h1>\n  </div>\n\n  <div class="home_buttons">\n    <a class="btn btn-success" href="#" role="button">Reports</a>\n    <a class="btn btn-success" href="#" role="button">Graduation Survey</a>\n    <a class="btn btn-success" href="#" role="button">IS News</a>\n  </div>\n\n')
>>>>>>> 385a8df006c363b089320eba393e99870f244917
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"uri": "index.html", "source_encoding": "utf-8", "line_map": {"36": 1, "53": 3, "41": 15, "59": 53, "29": 0, "47": 3}, "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/homepage/templates/index.html"}
=======
{"source_encoding": "utf-8", "uri": "index.html", "line_map": {"35": 1, "52": 3, "40": 15, "58": 52, "28": 0, "46": 3}, "filename": "/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/homepage/templates/index.html"}
>>>>>>> 385a8df006c363b089320eba393e99870f244917
__M_END_METADATA
"""
