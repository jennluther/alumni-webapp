# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493930725.715476
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/homepage/templates/base.htm'
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
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n    <title>surveys</title>\r\n    <link rel="icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/images/BYUlogo.png" type="image/gif" sizes="16x16">\r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <!-- <script src="/static/homepage/media/jquery.loadmodal.js"></script>\r\n    <script src="/static/homepage/media/jquery.form.min.js"></script> -->\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.full.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/sorrtable.js"></script>\r\n\r\n    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\r\n    <link rel="stylesheet" type="text/css" href="/static/homepage/media/jquery.datetimepicker.min.css"/>\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n    <header>\r\n\r\n      <nav class="navbar navbar-inverse navbar-static-top">\r\n        <div class="container-fluid">\r\n          <!-- Brand and toggle get grouped for better mobile display -->\r\n          <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n              <span class="sr-only">Toggle navigation</span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n            </button>\r\n            <a class="navbar-brand" href="#">Alumni Database</a>\r\n          </div>\r\n\r\n          <!-- Collect the nav links, forms, and other content for toggling -->\r\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n            <ul class="nav navbar-nav">\r\n              <li><a href="#">Reports</a></li>\r\n              <li><a href="#">Graduation Survey</a></li>\r\n              <li><a href="#">IS News</a></li>\r\n')
        if user.is_superuser:
            __M_writer('                <li><a href="/users/users/">Alumni</a></li>\r\n')
        __M_writer('            </ul>\r\n')
        if user.is_authenticated:
            __M_writer('              <ul class="nav navbar-nav navbar-right">\r\n                <li class=\'dropdown\'>\r\n                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">\r\n                    Welcome ')
            __M_writer(str( user.first_name ))
            __M_writer(' <span class="caret"></span>\r\n                  </a>\r\n                    <ul class="dropdown-menu">\r\n                      <li><a href="/users/account/"><i class="fa fa-user" aria-hidden="true"></i>My Account</a></li>\r\n                      <li><a href="/users/logout"><i class="fa fa-sign-out" aria-hidden="true"></i>Log Out</a></li>\r\n                    </ul>\r\n                </li>\r\n              </ul>\r\n')
        else:
            __M_writer('              <ul class="nav navbar-nav navbar-right">\r\n                <li><a href="/users/login/">Login</a></li>\r\n                <li><a href="/users/signup/">Sign up</a></li>\r\n              </ul>\r\n')
        __M_writer('          </div><!-- /.navbar-collapse -->\r\n        </div><!-- /.container-fluid -->\r\n      </nav>\r\n    </header>\r\n\r\n    ')
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
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/homepage/templates/base.htm", "line_map": {"66": 78, "72": 78, "78": 72, "18": 4, "20": 0, "31": 2, "32": 4, "33": 13, "34": 13, "35": 16, "36": 19, "37": 19, "38": 20, "39": 20, "40": 25, "41": 25, "42": 25, "43": 51, "44": 52, "45": 54, "46": 55, "47": 56, "48": 59, "49": 59, "50": 67, "51": 68, "52": 73, "57": 81, "58": 85, "59": 85, "60": 85}, "source_encoding": "utf-8", "uri": "base.htm"}
__M_END_METADATA
"""
