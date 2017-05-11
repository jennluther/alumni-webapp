# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1494522862.516905
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
        alumni = context.get('alumni', UNDEFINED)
        export_link = context.get('export_link', UNDEFINED)
        form = context.get('form', UNDEFINED)
        afilter = context.get('afilter', UNDEFINED)
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
        alumni = context.get('alumni', UNDEFINED)
        export_link = context.get('export_link', UNDEFINED)
        form = context.get('form', UNDEFINED)
        afilter = context.get('afilter', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer("\r\n<div class='container viewcontainer'>\r\n  <h1>Alumni:</h1>\r\n  <div>\r\n    ")
        __M_writer(str( form ))
        __M_writer('\r\n  </div><br>\r\n  <nav class=\'navbar nav\'>\r\n    <ul class="nav navbar-nav navbar-left">\r\n      <li class=\'dropdown\'>\r\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">\r\n          Actions <span class="caret"></span>\r\n        </a>\r\n          <ul class="dropdown-menu">\r\n            <li><a href="/users/user.create/">Create</a></li>\r\n            <li><a href="/users/upload">Upload Alumni Information </a></li>\r\n            <li><a href="')
        __M_writer(str( export_link ))
        __M_writer('">Export Alumni Information </a></li>\r\n          </ul>\r\n      </li>\r\n\r\n      <li class=\'dropdown\'>\r\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">\r\n          Filters <span class="caret"></span>\r\n        </a>\r\n          <ul class="dropdown-menu">\r\n            <li><a href="/users/users/all">All Users</a></li>\r\n            <li><a href="/users/users/completed">Exit Survey Completed</a></li>\r\n            <li><a href="/users/users/incomplete">Exit Survey Incomplete </a></li>\r\n            <li><a href="/users/users/MISM">MISM</a></li>\r\n            <li><a href="/users/users/BSIS">BSIS</a></li>\r\n          </ul>\r\n      </li>\r\n    </ul>\r\n  </nav>\r\n\r\n\r\n\r\n\r\n  <table class="table table-striped users sortable">\r\n      <tr>\r\n        <th>First Name</th>\r\n        <th>Last Name</th>\r\n        <th>Email</th>\r\n        <th>Program</th>\r\n        <th>Actions</th>\r\n      </tr>\r\n')
        for u in alumni:
            __M_writer('      <tr>\r\n        <td>')
            __M_writer(str( u.first_name ))
            __M_writer('</td>\r\n        <td>')
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
        __M_writer('  </table>\r\n\r\n\r\n<!-- Pagination -->\r\n')
        if alumni.has_other_pages:
            __M_writer('  <ul class="pagination">\r\n')
            if alumni.has_previous():
                __M_writer('      <li><a href="')
                __M_writer(str( alumni.previous_page_number() ))
                __M_writer('">&laquo;</a></li>\r\n')
            else:
                __M_writer('      <li class="disabled"><span>&laquo;</span></li>\r\n')
            for i in alumni.paginator.page_range:
                if alumni.number == i:
                    __M_writer('        <li class="active"><span>')
                    __M_writer(str( i ))
                    __M_writer('<span class="sr-only">(current)</span></span></li>\r\n')
                else:
                    __M_writer('        <li><a href="/users/users/')
                    __M_writer(str( afilter ))
                    __M_writer('/')
                    __M_writer(str( i ))
                    __M_writer('">')
                    __M_writer(str( i ))
                    __M_writer('</a></li>\r\n')
            if alumni.has_next():
                __M_writer('      <li><a href="')
                __M_writer(str( alumni.next_page_number() ))
                __M_writer('">&raquo;</a></li>\r\n')
            else:
                __M_writer('      <li class="disabled"><span>&raquo;</span></li>\r\n')
            __M_writer('  </ul>\r\n')
        __M_writer('</div>\r\n\r\n  <!-- Delete Modal -->\r\n<div class="modal fade" id="deleteModal" role="dialog">\r\n  <div class="modal-dialog">\r\n\r\n    <!-- Modal content-->\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n        <h4 class="modal-title">Confirm</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        <p>Are you sure you want to delete the alumni?</p>\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="real_delete" href="" class="btn btn-danger" type="submit">Yes</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">No</button>\r\n      </div>\r\n    </div>\r\n\r\n  </div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/MSM-IS-Web/Documents/Alumni Database/Program/alumni-webapp/users/templates/users.html", "uri": "users.html", "line_map": {"29": 0, "40": 1, "45": 116, "51": 4, "61": 4, "62": 8, "63": 8, "64": 19, "65": 19, "66": 49, "67": 50, "68": 51, "69": 51, "70": 52, "71": 52, "72": 53, "73": 53, "74": 54, "75": 55, "76": 55, "77": 55, "78": 56, "79": 57, "80": 59, "81": 60, "82": 60, "83": 61, "84": 61, "85": 62, "86": 62, "87": 66, "88": 70, "89": 71, "90": 72, "91": 73, "92": 73, "93": 73, "94": 74, "95": 75, "96": 77, "97": 78, "98": 79, "99": 79, "100": 79, "101": 80, "102": 81, "103": 81, "104": 81, "105": 81, "106": 81, "107": 81, "108": 81, "109": 84, "110": 85, "111": 85, "112": 85, "113": 86, "114": 87, "115": 89, "116": 91, "122": 116}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
