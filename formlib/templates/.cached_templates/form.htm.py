# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493827027.678042
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/formlib/templates/form.htm'
_template_uri = 'form.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        csrf_input = context.get('csrf_input', UNDEFINED)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str( django_mako_plus.link_css(self) ))
        __M_writer('\r\n\r\n<form action="')
        __M_writer(str( form.form_action or '' ))
        __M_writer('" method="')
        __M_writer(str( form.form_method ))
        __M_writer('" enctype="')
        __M_writer(str( form.form_enctype ))
        __M_writer('">\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( form.as_p() ))
        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( form.open_btn ))
        __M_writer(filters.html_escape(str( form.form_submit )))
        __M_writer(str( form.close_btn ))
        __M_writer('\r\n\r\n</form>\r\n\r\n\r\n')
        __M_writer(str( django_mako_plus.link_js(self) ))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "form.htm", "filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/formlib/templates/form.htm", "line_map": {"18": 0, "26": 2, "27": 2, "28": 4, "29": 4, "30": 4, "31": 4, "32": 4, "33": 4, "34": 7, "35": 7, "36": 7, "37": 10, "38": 10, "39": 10, "40": 13, "41": 13, "42": 13, "43": 13, "44": 13, "45": 19, "46": 19, "52": 46}}
__M_END_METADATA
"""
