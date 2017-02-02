# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1485540125.028631
_enable_loop = True
_template_filename = '/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/homepage/templates/base_ajax.htm'
_template_uri = '/homepage/templates/base_ajax.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  Sub-templates should place their ajax content here.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"36": 14, "37": 17, "38": 17, "44": 12, "17": 6, "50": 12, "19": 0, "56": 50, "28": 4, "29": 6, "30": 9, "31": 9}, "uri": "/homepage/templates/base_ajax.htm", "filename": "/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/homepage/templates/base_ajax.htm"}
__M_END_METADATA
"""
