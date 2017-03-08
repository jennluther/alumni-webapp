# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1487173727.52111
=======
<<<<<<< HEAD
_modified_time = 1488319516.4522314
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/users/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
import django_mako_plus
=======
_modified_time = 1485543109.335827
>>>>>>> 8b33fbe14b844ec104cd6f35130e4f4ad2ebfa51
_enable_loop = True
_template_filename = '/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/users/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
<<<<<<< HEAD
_exports = ['content', 'center_col', 'left_col', 'right_col']
=======
>>>>>>> 385a8df006c363b089320eba393e99870f244917
_exports = ['content']
>>>>>>> 8b33fbe14b844ec104cd6f35130e4f4ad2ebfa51


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
<<<<<<< HEAD
=======
<<<<<<< HEAD
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n    <title>users</title>\r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n    <header>\r\n      Welcome to the users app!\r\n    </header>\r\n\r\n    ')
=======
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
>>>>>>> 8b33fbe14b844ec104cd6f35130e4f4ad2ebfa51
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def center_col():
            return render_center_col(context._locals(__M_locals))
        def left_col():
            return render_left_col(context._locals(__M_locals))
        def right_col():
            return render_right_col(context._locals(__M_locals))
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
        __M_writer('\n\n  </head>\n  <body>\n\n    <header>\n\n      <nav class="navbar navbar-inverse navbar-static-top">\n        <div class="container-fluid">\n          <!-- Brand and toggle get grouped for better mobile display -->\n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n              <span class="sr-only">Toggle navigation</span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">Alumni Database</a>\n          </div>\n\n          <!-- Collect the nav links, forms, and other content for toggling -->\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n            <ul class="nav navbar-nav">\n              <li><a href="#">Reports</a></li>\n              <li><a href="#">Graduation Survey</a></li>\n              <li><a href="#">IS News</a></li>\n            </ul>\n\n            <ul class="nav navbar-nav navbar-right">\n              <li><a href="#">Login</a></li>\n              <li><a href="#">Sign up</a></li>\n            </ul>\n          </div><!-- /.navbar-collapse -->\n        </div><!-- /.container-fluid -->\n      </nav>\n    </header>\n\n    ')
>>>>>>> 385a8df006c363b089320eba393e99870f244917
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

<<<<<<< HEAD
        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
=======
        __M_writer('\n\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\n\n  </body>\n</html>\n')
>>>>>>> 385a8df006c363b089320eba393e99870f244917
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def center_col():
            return render_center_col(context)
        def left_col():
            return render_left_col(context)
        def right_col():
            return render_right_col(context)
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


def render_right_col(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_col():
            return render_right_col(context)
        __M_writer = context.writer()
<<<<<<< HEAD
        __M_writer('\n\n            ')
=======
<<<<<<< HEAD
        __M_writer('\r\n      Site content goes here in sub-templates.\r\n    ')
=======
        __M_writer('\n\n      Site content goes here in sub-templates.\n    ')
>>>>>>> 385a8df006c363b089320eba393e99870f244917
>>>>>>> 8b33fbe14b844ec104cd6f35130e4f4ad2ebfa51
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"filename": "/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/users/templates/base.htm", "uri": "base.htm", "line_map": {"115": 75, "70": 59, "103": 65, "75": 67, "80": 72, "17": 4, "19": 0, "85": 77, "91": 70, "97": 70, "35": 2, "36": 4, "37": 15, "38": 16, "39": 16, "40": 17, "41": 17, "42": 22, "43": 22, "44": 22, "109": 65, "49": 81, "50": 85, "51": 85, "52": 85, "121": 75, "58": 59, "127": 121}, "source_encoding": "utf-8"}
=======
<<<<<<< HEAD
{"uri": "base.htm", "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/users/templates/base.htm", "source_encoding": "utf-8", "line_map": {"32": 18, "33": 18, "34": 18, "39": 29, "40": 32, "41": 32, "42": 32, "48": 27, "18": 4, "20": 0, "54": 27, "60": 54, "29": 2, "30": 4, "31": 15}}
=======
{"source_encoding": "utf-8", "uri": "base.htm", "line_map": {"32": 16, "33": 16, "34": 17, "35": 17, "36": 22, "37": 22, "38": 22, "64": 58, "43": 62, "44": 66, "45": 66, "46": 66, "17": 4, "19": 0, "52": 59, "58": 59, "29": 2, "30": 4, "31": 15}, "filename": "/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/users/templates/base.htm"}
>>>>>>> 385a8df006c363b089320eba393e99870f244917
>>>>>>> 8b33fbe14b844ec104cd6f35130e4f4ad2ebfa51
__M_END_METADATA
"""
