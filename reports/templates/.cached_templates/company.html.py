# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1494254468.73625
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/reports/templates/company.html'
_template_uri = 'company.html'
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
        alumni = context.get('alumni', UNDEFINED)
        company = context.get('company', UNDEFINED)
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
        alumni = context.get('alumni', UNDEFINED)
        company = context.get('company', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n  <div class='container viewcontainer'>\r\n    <h2>Alumni that work at ")
        __M_writer(str( company.name ))
        __M_writer('</h2>\r\n    <nav class=\'navbar nav\'>\r\n      <ul class="nav navbar-nav navbar-left">\r\n        <li class=\'dropdown\'>\r\n          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">\r\n            Filters <span class="caret"></span>\r\n          </a>\r\n            <ul class="dropdown-menu">\r\n              <li><a href="/reports/company/')
        __M_writer(str( company.id ))
        __M_writer('">All Alumni</a></li>\r\n              <li><a href="/reports/company/')
        __M_writer(str( company.id ))
        __M_writer('/current">Current Job</a></li>\r\n              <li><a href="/reports/company/')
        __M_writer(str( company.id ))
        __M_writer('/past">Past Job</a></li>\r\n            </ul>\r\n        </li>\r\n      </ul>\r\n    </nav>\r\n    <table class="table table-striped users sortable">\r\n        <tr>\r\n          <th>First Name</th>\r\n          <th>Last Name</th>\r\n          <th>Current Job</th>\r\n          <th>View Info</th>\r\n        </tr>\r\n')
        for u in alumni:
            __M_writer('        <tr>\r\n          <td>')
            __M_writer(str( u.user.first_name ))
            __M_writer('</a>\r\n          <td>')
            __M_writer(str( u.user.last_name ))
            __M_writer('</td>\r\n          <td>')
            __M_writer(str( u.current_job ))
            __M_writer('</td>\r\n          <td>\r\n            <a href="/users/aluminfo/')
            __M_writer(str( u.user.id ))
            __M_writer('/">Details</a>\r\n          </td>\r\n        </tr>\r\n')
        __M_writer('    </table>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "company.html", "filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/reports/templates/company.html", "line_map": {"64": 16, "65": 16, "66": 28, "67": 29, "68": 30, "69": 30, "70": 31, "71": 31, "72": 32, "73": 32, "74": 34, "75": 34, "76": 38, "82": 76, "29": 0, "38": 1, "43": 40, "49": 4, "57": 4, "58": 6, "59": 6, "60": 14, "61": 14, "62": 15, "63": 15}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
