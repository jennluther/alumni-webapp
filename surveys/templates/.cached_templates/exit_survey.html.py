# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493736518.773503
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/surveys/templates/exit_survey.html'
_template_uri = 'exit_survey.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n<div class='viewcontainer container'>\r\n  <h1>Exit Survey</h1>\r\n\r\n        ")
        __M_writer(str( form ))
        __M_writer('\r\n  </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"48": 3, "37": 1, "55": 3, "56": 7, "57": 7, "42": 10, "29": 0, "63": 57}, "source_encoding": "utf-8", "filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/surveys/templates/exit_survey.html", "uri": "exit_survey.html"}
__M_END_METADATA
"""
