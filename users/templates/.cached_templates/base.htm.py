# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493916710.73323
_enable_loop = True
_template_filename = '/Users/Jenn/Programs/alumni-webapp/users/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import os, os.path, re, json
_exports = ['content', 'left_col', 'center_col', 'right_col']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def left_col():
            return render_left_col(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def right_col():
            return render_right_col(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def center_col():
            return render_center_col(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n\n    <title>surveys</title>\n\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.min.js"></script>\n\n    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\n\n  </head>\n  <body>\n\n    <header>\n\n      <nav class="navbar navbar-inverse navbar-static-top">\n        <div class="container-fluid">\n          <!-- Brand and toggle get grouped for better mobile display -->\n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n              <span class="sr-only">Toggle navigation</span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">Alumni Database</a>\n          </div>\n\n          <!-- Collect the nav links, forms, and other content for toggling -->\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n            <ul class="nav navbar-nav">\n              <li><a href="#">Reports</a></li>\n              <li><a href="#">Graduation Survey</a></li>\n              <li><a href="#">IS News</a></li>\n            </ul>\n')
        if user.is_authenticated:
            __M_writer('              <ul class="nav navbar-nav navbar-right">\n                <li><a href="#">Welcome ')
            __M_writer(str( user.first_name ))
            __M_writer('</a></li>\n              </ul>\n')
        else:
            __M_writer('              <ul class="nav navbar-nav navbar-right">\n                <li><a href="#">Login</a></li>\n                <li><a href="#">Sign up</a></li>\n              </ul>\n')
        __M_writer('          </div><!-- /.navbar-collapse -->\n        </div><!-- /.container-fluid -->\n      </nav>\n    </header>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\n\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_col():
            return render_right_col(context)
        def content():
            return render_content(context)
        def center_col():
            return render_center_col(context)
        def left_col():
            return render_left_col(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n      <div class="container">\n        <div class="row">\n          <div class="col-md-2">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_col'):
            context['self'].left_col(**pageargs)
        

        __M_writer('<!--left_col-->\n          </div>\n          <div class="col-md-8">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_col'):
            context['self'].center_col(**pageargs)
        

        __M_writer('<!--center_col-->\n          </div>\n          <div class="col-md-2">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_col'):
            context['self'].right_col(**pageargs)
        

        __M_writer('<!--right_col-->\n          </div>\n        </div>\n      </div>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_col(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_col():
            return render_left_col(context)
        __M_writer = context.writer()
        __M_writer('\n\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_col(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_col():
            return render_center_col(context)
        __M_writer = context.writer()
        __M_writer('\n\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_col(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_col():
            return render_right_col(context)
        __M_writer = context.writer()
        __M_writer('\n\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jenn/Programs/alumni-webapp/users/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 4, "20": 0, "37": 2, "38": 4, "39": 15, "40": 16, "41": 16, "42": 17, "43": 17, "44": 22, "45": 22, "46": 22, "47": 49, "48": 50, "49": 51, "50": 51, "51": 53, "52": 54, "53": 59, "58": 86, "59": 90, "60": 90, "61": 90, "67": 64, "79": 64, "84": 72, "89": 77, "94": 82, "100": 70, "106": 70, "112": 75, "118": 75, "124": 80, "130": 80, "136": 130}}
__M_END_METADATA
"""
