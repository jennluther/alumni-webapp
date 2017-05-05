# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1494021835.997322
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/reports/templates/companies.html'
_template_uri = 'companies.html'
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
        companies = context.get('companies', UNDEFINED)
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
        companies = context.get('companies', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n  <div class='viewcontainer container'>\r\n    <h2>Compaines where our Alumni are</h2>\r\n")
        for c in companies:
            __M_writer("      <h3><a href='company/")
            __M_writer(str( c.id ))
            __M_writer("'>")
            __M_writer(str( c.name ))
            __M_writer('</a></h3>\r\n')
        __M_writer('  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/reports/templates/companies.html", "line_map": {"68": 62, "37": 1, "42": 11, "61": 8, "48": 4, "55": 4, "56": 7, "57": 8, "58": 8, "59": 8, "60": 8, "29": 0, "62": 10}, "source_encoding": "utf-8", "uri": "companies.html"}
__M_END_METADATA
"""
