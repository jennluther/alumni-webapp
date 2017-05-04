# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493934924.140646
_enable_loop = True
_template_filename = 'C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/users.html'
_template_uri = 'users.html'
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
        form = context.get('form', UNDEFINED)
        alumni = context.get('alumni', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        alumni = context.get('alumni', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n<div class='container viewcontainer'>\r\n  <h1>Alumni:</h1>\r\n  <div>\r\n    ")
        __M_writer(str( form ))
        __M_writer('\r\n  </div><br>\r\n  <nav class=\'navbar nav\'>\r\n    <ul class="nav navbar-nav navbar-left">\r\n      <li class=\'dropdown\'>\r\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">\r\n          Actions <span class="caret"></span>\r\n        </a>\r\n          <ul class="dropdown-menu">\r\n            <li><a href="/users/user.create/">Create</a></li>\r\n            <li><a href="/users/upload">Upload Alumni Information </a></li>\r\n          </ul>\r\n      </li>\r\n\r\n      <li class=\'dropdown\'>\r\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">\r\n          Filters <span class="caret"></span>\r\n        </a>\r\n          <ul class="dropdown-menu">\r\n            <li><a href="/users/users">All Users</a></li>\r\n            <li><a href="/users/users/completed">Exit Survey Completed</a></li>\r\n            <li><a href="/users/users/incomplete">Exit Survey Incomplete </a></li>\r\n            <li><a href="/users/users/MISM">MISM</a></li>\r\n            <li><a href="/users/users/BSIS">BSIS</a></li>\r\n          </ul>\r\n      </li>\r\n    </ul>\r\n  </nav>\r\n\r\n\r\n\r\n\r\n  <table class="table table-striped users sortable">\r\n      <tr>\r\n        <th>First Name</th>\r\n        <th>Last Name</th>\r\n        <th>Email</th>\r\n        <th>Program</th>\r\n        <th>Actions</th>\r\n      </tr>\r\n')
        for u in alumni:
            __M_writer('      <tr>\r\n        <td>')
            __M_writer(str( u.first_name ))
            __M_writer('</a>\r\n        <td>')
            __M_writer(str( u.last_name ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( u.email ))
            __M_writer('</td>\r\n')
            if u.program:
                __M_writer('          <td>')
                __M_writer(str( u.program ))
                __M_writer('</td>\r\n')
            else:
                __M_writer('          <td> - </td>\r\n')
            __M_writer('        <td>\r\n          <a href="/users/aluminfo/')
            __M_writer(str( u.id ))
            __M_writer('/">Details</a> |\r\n          <a href="/users/user/')
            __M_writer(str( u.id ))
            __M_writer('/">Edit</a> |\r\n          <a href="/users/user.delete/')
            __M_writer(str( u.id ))
            __M_writer('/" class="delete_link">Delete</a>\r\n        </td>\r\n      </tr>\r\n')
        __M_writer('  </table>\r\n</div>\r\n\r\n  <!-- Delete Modal -->\r\n<div class="modal fade" id="deleteModal" role="dialog">\r\n  <div class="modal-dialog">\r\n\r\n    <!-- Modal content-->\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n        <h4 class="modal-title">Confirm</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        <p>Are you sure you want to delete the alumni?</p>\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n      </div>\r\n    </div>\r\n\r\n  </div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/users.html", "uri": "users.html", "source_encoding": "utf-8", "line_map": {"64": 51, "65": 51, "66": 52, "67": 52, "68": 53, "69": 54, "70": 54, "71": 54, "72": 55, "73": 56, "74": 58, "75": 59, "76": 59, "77": 60, "78": 60, "79": 61, "80": 61, "81": 65, "87": 81, "29": 0, "38": 1, "43": 91, "49": 4, "57": 4, "58": 8, "59": 8, "60": 48, "61": 49, "62": 50, "63": 50}}
__M_END_METADATA
"""
