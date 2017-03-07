# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1488319592.6784484
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/formlib/templates/form.htm'
_template_uri = 'form.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str( django_mako_plus.link_css(self) ))
        __M_writer('\n\n<form action="')
        __M_writer(str( form.form_action or '' ))
        __M_writer('" method="')
        __M_writer(str( form.form_method ))
        __M_writer('">\n\n')
        __M_writer('    ')
        __M_writer(str( csrf_input ))
        __M_writer('\n\n')
        __M_writer('    ')
        __M_writer(str( form.as_p() ))
        __M_writer('\n\n')
        __M_writer('    <p class="text-center"><button type="submit" class="btn btn-primary">')
        __M_writer(filters.html_escape(str( form.form_submit )))
        __M_writer('</button></p>\n\n</form>\n\n\n')
        __M_writer(str( django_mako_plus.link_js(self) ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "form.htm", "line_map": {"32": 7, "33": 7, "34": 7, "35": 10, "36": 10, "37": 10, "38": 13, "39": 13, "40": 13, "41": 19, "42": 19, "48": 42, "18": 0, "26": 2, "27": 2, "28": 4, "29": 4, "30": 4, "31": 4}, "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/formlib/templates/form.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
