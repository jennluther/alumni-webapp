# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490217267.290299
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import os, os.path, re, json
_exports = ['center_col', 'content', 'left_col', 'right_col']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def right_col():
            return render_right_col(context._locals(__M_locals))
        def center_col():
            return render_center_col(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def left_col():
            return render_left_col(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n    <title>surveys</title>\r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.min.js"></script>\r\n\r\n    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n    <header>\r\n\r\n      <nav class="navbar navbar-inverse navbar-static-top">\r\n        <div class="container-fluid">\r\n          <!-- Brand and toggle get grouped for better mobile display -->\r\n          <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n              <span class="sr-only">Toggle navigation</span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n            </button>\r\n            <a class="navbar-brand" href="#">Alumni Database</a>\r\n          </div>\r\n\r\n          <!-- Collect the nav links, forms, and other content for toggling -->\r\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n            <ul class="nav navbar-nav">\r\n              <li><a href="#">Reports</a></li>\r\n              <li><a href="#">Graduation Survey</a></li>\r\n              <li><a href="#">IS News</a></li>\r\n            </ul>\r\n\r\n            <ul class="nav navbar-nav navbar-right">\r\n              <li><a href="#">Login</a></li>\r\n              <li><a href="#">Sign up</a></li>\r\n            </ul>\r\n          </div><!-- /.navbar-collapse -->\r\n        </div><!-- /.container-fluid -->\r\n      </nav>\r\n    </header>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_col(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_col():
            return render_center_col(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_col():
            return render_center_col(context)
        def content():
            return render_content(context)
        def left_col():
            return render_left_col(context)
        def right_col():
            return render_right_col(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n      <div class="container">\r\n        <div class="row">\r\n          <div class="col-md-2">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_col'):
            context['self'].left_col(**pageargs)
        

        __M_writer('<!--left_col-->\r\n          </div>\r\n          <div class="col-md-8">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_col'):
            context['self'].center_col(**pageargs)
        

        __M_writer('<!--center_col-->\r\n          </div>\r\n          <div class="col-md-2">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_col'):
            context['self'].right_col(**pageargs)
        

        __M_writer('<!--right_col-->\r\n          </div>\r\n        </div>\r\n      </div>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_col(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_col():
            return render_left_col(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_col(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_col():
            return render_right_col(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "base.htm", "filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/base.htm", "line_map": {"128": 122, "65": 70, "71": 59, "18": 4, "83": 59, "20": 0, "88": 67, "93": 72, "98": 77, "36": 2, "37": 4, "38": 15, "39": 16, "40": 16, "41": 17, "42": 17, "43": 22, "44": 22, "45": 22, "110": 65, "104": 65, "50": 81, "51": 85, "52": 85, "53": 85, "116": 75, "122": 75, "59": 70}}
__M_END_METADATA
"""
