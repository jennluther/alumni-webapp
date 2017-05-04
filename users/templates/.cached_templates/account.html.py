# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493915784.8010309
_enable_loop = True
_template_filename = '/Users/Jenn/Programs/alumni-webapp/users/templates/account.html'
_template_uri = 'account.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <h1>Your Account:</h1>\n  <h2>Personal Information:</h2>\n  <table class="table table-striped">\n    <tr>\n      <th>First Name</th>\n      <th>Last Name</th>\n      <th>City</th>\n      <th>State</th>\n      <th>Email</th>\n    </tr>\n    <tr>\n      <td>')
        __M_writer(str( user.first_name ))
        __M_writer('</td>\n      <td>')
        __M_writer(str( user.last_name ))
        __M_writer('</td>\n      <td>')
        __M_writer(str( user.city ))
        __M_writer('</td>\n      <td>')
        __M_writer(str( user.state ))
        __M_writer('</td>\n      <td>')
        __M_writer(str( user.email ))
        __M_writer('</td>\n    </tr>\n  </table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jenn/Programs/alumni-webapp/users/templates/account.html", "uri": "account.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 24, "48": 4, "55": 4, "56": 16, "57": 16, "58": 17, "59": 17, "60": 18, "61": 18, "62": 19, "63": 19, "64": 20, "65": 20, "71": 65}}
__M_END_METADATA
"""
