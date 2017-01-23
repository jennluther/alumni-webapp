# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1485205617.1688616
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/confirm_info.html'
_template_uri = 'confirm_info.html'
_source_encoding = 'utf-8'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
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
        __M_writer = context.writer()
        __M_writer('\r\n<head>\r\n  <script type=\'text/javascript\'>\r\n    function addFields(){\r\n      //Number of inputs to create\r\n      var number = document.getElementById("intern_fields").value;\r\n      //Area where dynamic content will be placed\r\n      var intern_fields = document.getElementById("intern_fields");\r\n    }\r\n    for (i=0; i<number; i++){\r\n      //Append a node with random text\r\n      intern_fields.appendChild(document.createTextNode("Internship " + (i+1)));\r\n      //Create an <input> element, set its type and name attributes\r\n      var input = document.createElement("input");\r\n      input.type = "text";\r\n      input.name = "intern" + i;\r\n      intern_fields.appendChild(document.createElement("br"));\r\n    }\r\n  </script>\r\n</head>\r\n\r\n<body>\r\n  <div class="col-lg-offset-2 col-lg-8"\r\n    <form action="/confirm-info/" method="post">\r\n      <h1>Contact Information</h1>\r\n\r\n      <div class="form-group">\r\n        <label for="first_name">First name: </label>\r\n        <input id="first_name" type="text" class="form-control" name="first_name" value="">\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="last_name">Last name: </label>\r\n        <input id="last_name" type="text" class="form-control" name="last_name" value="">\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="email">Email: </label>\r\n        <input id="email" type="text" class="form-control" name="email" value="">\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="phone">Phone number: </label>\r\n        <input id="phone" type="text" class="form-control" name="phone" value="">\r\n      </div>\r\n\r\n      <h1>Job Information</h1>\r\n\r\n      <div class="form-group">\r\n        <label for="company">Company: </label><!--make this field give suggested companies that are already in Database-->\r\n        <input id="company" type="text" class="form-control" name="company" value="">\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="salary">Salary: </label>\r\n        <input id="salary" type="text" class="form-control" name="salary" value="">\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="city">City: </label>\r\n        <input id="city" type="text" class="form-control" name="city" value="">\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="state">State: </label><!--link to State list and make it a drop down-->\r\n        <input id="state" type="text" class="form-control" name="state" value="">\r\n      </div>\r\n\r\n      <h1>Internship Information</h1>\r\n\r\n      <div class="form-group">\r\n        <label for="intern_fields">How many internships did you complete?</label><!--make this a drop down of numbers-->\r\n        <input id="intern_fields" type="text" class="form-control" name="intern_fields">\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="intern_company">Company: </label><!--make this field give suggested companies that are already in Database-->\r\n        <input id="intern_company" type="text" class="form-control" name="intern_company" value="">\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="how_obtained">How did you obtain your internship? </label><!--drop down list obtain-->\r\n        <input id="how_obtained" type="text" class="form-control" name="how_obtained" value="">\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="intern_company">How much time did you spend looking for your internship? </label><!--drop down list obtain-->\r\n        <input id="intern_company" type="text" class="form-control" name="intern_company" value="">\r\n      </div>\r\n\r\n        <input type="submit" value="Save">\r\n    </form>\r\n  </div>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/confirm_info.html", "uri": "confirm_info.html", "line_map": {"35": 1, "52": 3, "40": 98, "58": 52, "28": 0, "46": 3}}
__M_END_METADATA
"""
