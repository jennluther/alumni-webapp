# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1493907467.088383
_enable_loop = True
_template_filename = '/Users/Jenn/Programs/alumni-webapp/users/templates/users.html'
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
        form = context.get('form', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\n<div class='container viewcontainer'>\n  <h1>Alumni:</h1>\n  <div>\n    ")
        __M_writer(str( form ))
        __M_writer('\n  </div><br>\n  <p>\n    <strong>Actions:</strong>\n    <a href="/users/user.create/" class="btn btn-primary">Create</a>\n    <a href="/users/upload" class = "btn btn-primary">Upload Alumni Information </a>\n  </p>\n  <p>\n    <strong>Filters:</strong>\n    <a href="/users/users" class="btn btn-primary">All Users</a>\n    <a href="/users/users/completed" class="btn btn-primary">Exit Survey Completed</a>\n    <a href="/users/users/incomplete" class = "btn btn-primary">Exit Survey Incomplete </a>\n    <a href="/users/users/MISM" class = "btn btn-primary">MISM</a>\n    <a href="/users/users/BSIS" class = "btn btn-primary">BSIS</a>\n  </p>\n\n\n\n  <table class="table table-striped users sortable">\n      <tr>\n        <th>First Name</th>\n        <th>Last Name</th>\n        <th>Email</th>\n        <th>Program</th>\n        <th>Actions</th>\n      </tr>\n')
        for u in users:
            __M_writer('      <tr>\n        <td>')
            __M_writer(str( u.first_name ))
            __M_writer('</a>\n        <td>')
            __M_writer(str( u.last_name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( u.email ))
            __M_writer('</td>\n')
            if u.program:
                __M_writer('          <td>')
                __M_writer(str( u.program ))
                __M_writer('</td>\n')
            else:
                __M_writer('          <td> - </td>\n')
            __M_writer('        <td>\n          <a href="/users/aluminfo/')
            __M_writer(str( u.id ))
            __M_writer('/">Details</a> |\n          <a href="/users/user/')
            __M_writer(str( u.id ))
            __M_writer('/">Edit</a> |\n          <a href="/users/user.delete/')
            __M_writer(str( u.id ))
            __M_writer('/" class="delete_link">Delete</a>\n        </td>\n      </tr>\n')
        __M_writer('  </table>\n</div>\n\n  <!-- Delete Modal -->\n<div class="modal fade" id="deleteModal" role="dialog">\n  <div class="modal-dialog">\n\n    <!-- Modal content-->\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal">&times;</button>\n        <h4 class="modal-title">Confirm</h4>\n      </div>\n      <div class="modal-body">\n        <p>Are you sure you want to delete the user?</p>\n      </div>\n      <div class="modal-footer">\n        <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\n        <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\n      </div>\n    </div>\n\n  </div>\n</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jenn/Programs/alumni-webapp/users/templates/users.html", "uri": "users.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 77, "49": 4, "57": 4, "58": 8, "59": 8, "60": 34, "61": 35, "62": 36, "63": 36, "64": 37, "65": 37, "66": 38, "67": 38, "68": 39, "69": 40, "70": 40, "71": 40, "72": 41, "73": 42, "74": 44, "75": 45, "76": 45, "77": 46, "78": 46, "79": 47, "80": 47, "81": 51, "87": 81}}
__M_END_METADATA
"""
