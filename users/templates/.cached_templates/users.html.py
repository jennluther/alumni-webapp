# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493653313.172672
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
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class=\'container viewcontainer\'>\r\n  <h1>Users:</h1>\r\n\r\n  <a href="/users/user.create/" class="btn btn-primary">Create</a>\r\n  <a href="/users/users" class="btn btn-primary">All Users</a>\r\n  <a href="/users/users/completed" class="btn btn-primary">Filter: Exit Survey Completed</a>\r\n  <a href="/users/users/incomplete" class = "btn btn-primary">Filter: Exit Survey Incomplete </a>\r\n  <a href="/users/upload" class = "btn btn-primary">Upload Alumni Information </a>\r\n\r\n\r\n  <table class="table table-striped users">\r\n      <tr>\r\n        <th>First Name</th>\r\n        <th>Last Name</th>\r\n        <th>Email</th>\r\n        <th>Phone Number</th>\r\n        <th>City</th>\r\n        <th>State</th>\r\n        <th>Actions</th>\r\n      </tr>\r\n')
        for u in users:
            __M_writer('      <tr>\r\n        <td>')
            __M_writer(str( u.first_name ))
            __M_writer('</a>\r\n        <td>')
            __M_writer(str( u.last_name ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( u.email ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( u.phone ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( u.city ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( u.state ))
            __M_writer('</td>\r\n        <td>\r\n          <a href="/users/aluminfo/')
            __M_writer(str( u.id ))
            __M_writer('/">Details</a> |\r\n          <a href="/users/user/')
            __M_writer(str( u.id ))
            __M_writer('/">Edit</a> |\r\n          <a href="/users/user.delete/')
            __M_writer(str( u.id ))
            __M_writer('/" class="delete_link">Delete</a>\r\n        </td>\r\n      </tr>\r\n')
        __M_writer('  </table>\r\n</div>\r\n\r\n  <!-- Delete Modal -->\r\n<div class="modal fade" id="deleteModal" role="dialog">\r\n  <div class="modal-dialog">\r\n\r\n    <!-- Modal content-->\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n        <h4 class="modal-title">Confirm</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        <p>Are you sure you want to delete the user?</p>\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n      </div>\r\n    </div>\r\n\r\n  </div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/users.html", "line_map": {"64": 30, "65": 30, "66": 31, "67": 31, "68": 32, "69": 32, "70": 34, "71": 34, "72": 35, "73": 35, "74": 36, "75": 36, "76": 40, "82": 76, "29": 0, "37": 1, "42": 66, "48": 4, "55": 4, "56": 25, "57": 26, "58": 27, "59": 27, "60": 28, "61": 28, "62": 29, "63": 29}, "uri": "users.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
