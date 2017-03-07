# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1488578297.6497567
=======
_modified_time = 1485539810.060318
>>>>>>> 385a8df006c363b089320eba393e99870f244917
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import os, os.path, re, json
_exports = ['content']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
<<<<<<< HEAD
=======
        def content():
            return render_content(context._locals(__M_locals))
>>>>>>> 385a8df006c363b089320eba393e99870f244917
        self = context.get('self', UNDEFINED)
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
<<<<<<< HEAD
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n    <header>\r\n\r\n      <nav class="navbar navbar-inverse navbar-static-top">\r\n        <div class="container-fluid">\r\n          <!-- Brand and toggle get grouped for better mobile display -->\r\n          <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n              <span class="sr-only">Toggle navigation</span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n            </button>\r\n            <a class="navbar-brand" href="#">Alumni Database</a>\r\n          </div>\r\n\r\n          <!-- Collect the nav links, forms, and other content for toggling -->\r\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n            <ul class="nav navbar-nav">\r\n              <li><a href="#">Reports</a></li>\r\n              <li><a href="#">Graduation Survey</a></li>\r\n              <li><a href="#">IS News</a></li>\r\n            </ul>\r\n\r\n            <ul class="nav navbar-nav navbar-right">\r\n              <li><a href="#">Login</a></li>\r\n              <li><a href="#">Sign up</a></li>\r\n            </ul>\r\n          </div><!-- /.navbar-collapse -->\r\n        </div><!-- /.container-fluid -->\r\n      </nav>\r\n    </header>\r\n\r\n    ')
=======
        __M_writer('\n\n  </head>\n  <body>\n\n    <header>\n\n      <nav class="navbar navbar-inverse navbar-static-top">\n        <div class="container-fluid">\n          <!-- Brand and toggle get grouped for better mobile display -->\n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n              <span class="sr-only">Toggle navigation</span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">Alumni Database</a>\n          </div>\n\n          <!-- Collect the nav links, forms, and other content for toggling -->\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n            <ul class="nav navbar-nav">\n              <li><a href="#">Reports</a></li>\n              <li><a href="#">Graduation Survey</a></li>\n              <li><a href="#">IS News</a></li>\n            </ul>\n\n            <ul class="nav navbar-nav navbar-right">\n              <li><a href="#">Sign up</a></li>\n              <li><a href="/users/login/">Login</a></li>\n            </ul>\n          </div><!-- /.navbar-collapse -->\n        </div><!-- /.container-fluid -->\n      </nav>\n    </header>\n\n    ')
>>>>>>> 385a8df006c363b089320eba393e99870f244917
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n      Site content goes here in sub-templates.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"uri": "base.htm", "source_encoding": "utf-8", "line_map": {"32": 15, "33": 16, "34": 16, "35": 17, "36": 17, "37": 22, "38": 22, "39": 22, "44": 62, "45": 66, "46": 66, "47": 66, "18": 4, "20": 0, "53": 59, "59": 59, "65": 59, "30": 2, "31": 4}, "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/homepage/templates/base.htm"}
=======
{"line_map": {"32": 16, "33": 16, "34": 17, "35": 17, "36": 22, "37": 22, "38": 22, "64": 58, "43": 62, "44": 66, "45": 66, "46": 66, "17": 4, "19": 0, "52": 59, "58": 59, "29": 2, "30": 4, "31": 15}, "source_encoding": "utf-8", "filename": "/Users/beckyrichards/Documents/Development/alumni-webapp/alumni-webapp/homepage/templates/base.htm", "uri": "base.htm"}
>>>>>>> 385a8df006c363b089320eba393e99870f244917
__M_END_METADATA
"""
