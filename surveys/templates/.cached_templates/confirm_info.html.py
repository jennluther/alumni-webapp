# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484349397.385737
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/confirm_info.html'
_template_uri = 'confirm_info.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<html>\r\n<head>\r\n  <script type=\'text/javascript\'>\r\n    function addFields(){\r\n      //Number of inputs to create\r\n      var number = document.getElementById("intern_fields").value;\r\n      //Area where dynamic content will be placed\r\n      var intern_fields = document.getElementById("intern_fields");\r\n    }\r\n    for (i=0; i<number; i++){\r\n      //Append a node with random text\r\n      intern_fields.appendChild(document.createTextNode("Internship " + (i+1)));\r\n      //Create an <input> element, set its type and name attributes\r\n      var input = document.createElement("input");\r\n      input.type = "text";\r\n      input.name = "intern" + i;\r\n      intern_fields.appendChild(document.createElement("br"));\r\n    }\r\n  </script>\r\n</head>\r\n\r\n<body>\r\n<form action="/confirm-info/" method="post">\r\n  <h1>Contact Information</h1>\r\n    <label for="first_name">First name: </label>\r\n    <input id="first_name" type="text" name="first_name" value="{{ current_fname }}">\r\n    <label for="last_name">Last name: </label>\r\n    <input id="last_name" type="text" name="last_name" value="{{ current_lname }}">\r\n    <label for="email">Email: </label>\r\n    <input id="email" type="text" name="email" value="{{ current_email }}">\r\n    <label for="phone">Phone number: </label>\r\n    <input id="phone" type="text" name="phone" value="{{ current_phone }}">\r\n\r\n  <h1>Job Information</h1>\r\n    <label for="company">Company: </label><!--make this field give suggested companies that are already in Database-->\r\n    <input id="company" type="text" name="company" value="{{ current_company }}">\r\n    <label for="salary">Salary: </label>\r\n    <input id="salary" type="text" name="salary" value="{{ current_salary }}">\r\n    <label for="city">City: </label>\r\n    <input id="city" type="text" name="city" value="{{ current_city }}">\r\n    <label for="state">State: </label><!--link to State list and make it a drop down-->\r\n    <input id="state" type="text" name="state" value="{{ current_state }}">\r\n\r\n  <h1>Internship Information</h1>\r\n    <label for="intern_fields">If multiple, how many internships did you complete?</label><!--make this a drop down of numbers-->\r\n    <input id="intern_fields" type="text" name="intern_fields">\r\n    <label for="intern_company">Company: </label><!--make this field give suggested companies that are already in Database-->\r\n    <input id="intern_company" type="text" name="intern_company" value="{{ current_intern_company }}">\r\n\r\n    <input type="submit" value="Save">\r\n</form>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"17": 0, "28": 22, "22": 1}, "filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/confirm_info.html", "uri": "confirm_info.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
