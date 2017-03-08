# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487173923.817152
_enable_loop = True
_template_filename = '/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/users/templates/signup.html'
_template_uri = 'signup.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['center_col']


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
        def center_col():
            return render_center_col(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_col'):
            context['self'].center_col(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_col(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_col():
            return render_center_col(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h1 class="text-center">Sign Up</h1>\n  <br></br>\n  <form class = "text-center" method="POST">\n    <table align="center" id="myform">\n      ')
        __M_writer(str( form.as_table() ))
        __M_writer('\n    </table>\n    <br></br>\n    <input type="submit" class="btn btn-warning" value="Save"/>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/users/templates/signup.html", "uri": "signup.html", "line_map": {"36": 1, "54": 3, "55": 8, "56": 8, "41": 13, "28": 0, "62": 56, "47": 3}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
