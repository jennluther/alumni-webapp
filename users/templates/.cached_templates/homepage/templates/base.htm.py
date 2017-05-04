# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493911521.671487
_enable_loop = True
_template_filename = '/Users/Jenn/Programs/alumni-webapp/homepage/templates/base.htm'
_template_uri = 'homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import os, os.path, re, json
_exports = ['content']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n\n    <title>surveys</title>\n    <link rel="icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/images/BYUlogo.png" type="image/gif" sizes="16x16">\n\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <!-- <script src="/static/homepage/media/jquery.loadmodal.js"></script>\n    <script src="/static/homepage/media/jquery.form.min.js"></script> -->\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.full.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/sorrtable.js"></script>\n\n    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n    <link rel="stylesheet" type="text/css" href="/static/homepage/media/jquery.datetimepicker.min.css"/>\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\n\n  </head>\n  <body>\n\n    <header>\n\n      <nav class="navbar navbar-inverse navbar-static-top">\n        <div class="container-fluid">\n          <!-- Brand and toggle get grouped for better mobile display -->\n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n              <span class="sr-only">Toggle navigation</span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">Alumni Database</a>\n          </div>\n\n          <!-- Collect the nav links, forms, and other content for toggling -->\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n            <ul class="nav navbar-nav">\n              <li><a href="#">Reports</a></li>\n              <li><a href="#">Graduation Survey</a></li>\n              <li><a href="#">IS News</a></li>\n              <li><a href="/users/users/">Alumni</a></li>\n            </ul>\n')
        if user.is_authenticated:
            __M_writer('              <ul class="nav navbar-nav navbar-right">\n                <li class=\'dropdown\'>\n                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">\n                    Welcome ')
            __M_writer(str( user.first_name ))
            __M_writer(' <span class="caret"></span>\n                  </a>\n                    <ul class="dropdown-menu">\n                      <li><a href="/users/user/')
            __M_writer(str( user.id ))
            __M_writer('"><i class="fa fa-user" aria-hidden="true"></i>My Account</a></li>\n                      <li><a href="/users/logout"><i class="fa fa-sign-out" aria-hidden="true"></i>Log Out</a></li>\n                    </ul>\n                </li>\n              </ul>\n')
        else:
            __M_writer('              <ul class="nav navbar-nav navbar-right">\n                <li><a href="/users/login/">Login</a></li>\n                <li><a href="/users/create/">Sign up</a></li>\n              </ul>\n')
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n      Site content goes here in sub-templates.\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jenn/Programs/alumni-webapp/homepage/templates/base.htm", "uri": "homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 4, "20": 0, "31": 2, "32": 4, "33": 13, "34": 13, "35": 16, "36": 19, "37": 19, "38": 20, "39": 20, "40": 25, "41": 25, "42": 25, "43": 53, "44": 54, "45": 57, "46": 57, "47": 60, "48": 60, "49": 65, "50": 66, "51": 71, "56": 79, "57": 83, "58": 83, "59": 83, "65": 76, "71": 76, "77": 71}}
__M_END_METADATA
"""
