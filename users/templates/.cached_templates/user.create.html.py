# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD:users/templates/.cached_templates/user.create.html.py
_modified_time = 1488319516.4292138
=======
_modified_time = 1485542978.852324
>>>>>>> 385a8df006c363b089320eba393e99870f244917:surveys/templates/.cached_templates/index.html.py
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/users/templates/user.create.html'
_template_uri = 'user.create.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
import django_mako_plus
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
<<<<<<< HEAD:users/templates/.cached_templates/user.create.html.py
        __M_writer('\r\n  <h1>Create User here:</h1>\r\n\r\n  ')
        __M_writer(str( form ))
        __M_writer('\r\n\r\n')
=======
        __M_writer('\n\n  <div class="content">\n    <h1>Graduation Survey. </h1>\n  </div>\n\n  <div class="home_buttons">\n\n    <a class="btn btn-success btn-lg" href="#" role="button">Take the survey</a>\n\n  </div>\n\n')
>>>>>>> 385a8df006c363b089320eba393e99870f244917:surveys/templates/.cached_templates/index.html.py
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD:users/templates/.cached_templates/user.create.html.py
{"uri": "user.create.html", "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/users/templates/user.create.html", "source_encoding": "utf-8", "line_map": {"48": 4, "37": 1, "55": 4, "56": 7, "57": 7, "42": 9, "29": 0, "63": 57}}
=======
{"source_encoding": "utf-8", "uri": "index.html", "line_map": {"35": 1, "52": 3, "40": 15, "58": 52, "28": 0, "46": 3}, "filename": "/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/surveys/templates/index.html"}
>>>>>>> 385a8df006c363b089320eba393e99870f244917:surveys/templates/.cached_templates/index.html.py
__M_END_METADATA
"""
