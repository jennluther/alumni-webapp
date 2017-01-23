# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484868579.8827355
_enable_loop = True
_template_filename = 'C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/exit_survey.html'
_template_uri = 'exit_survey.html'
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
        models = context.get('models', UNDEFINED)
        PROGRAM_INTRO = context.get('PROGRAM_INTRO', UNDEFINED)
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
        models = context.get('models', UNDEFINED)
        PROGRAM_INTRO = context.get('PROGRAM_INTRO', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<form action="/contact-info/" method="post">\r\n  <h1>Job Information</h1>\r\n\r\n    <label for="offers_received">How many full-time offers did you receive? </label><br> <!--drop down of numbers-->\r\n    <input id="offers_received" type="text" name="offers_received" value=""><br><br>\r\n\r\n    <label for="company">Which company did you accept an offer with? </label><br><!--make this field give suggested companies that are already in Database-->\r\n    <input id="company" type="text" name="company" value=""><br><br>\r\n\r\n    <label for="expected_salary">What is your expected salary? </label><br>\r\n    <input id="expected_salary" type="text" name="exptected_salary" value=""><br><br>\r\n\r\n    <label for="position_title">What is your position title? </label><br>\r\n    <input id="position_title" type="text" name="position_title" value=""><br><br>\r\n\r\n    <label for="position_description">Which of the following best describes your position? </label><br> <!--list of possible job descriptions-->\r\n    <input id="position_description" type="text" name="position_description" value=""><br><br>\r\n    <!--alternate position description that can take the place of the position_description-->\r\n\r\n    <!--I don\'t know if we need to do anything to allow the "other" submition to have the same tags as the position_description-->\r\n    <label for="position_description">If other, list here: </label><br> <!--list of possible job descriptions-->\r\n    <input id="position_description" type="text" name="position_description" value=""><br><br>\r\n\r\n    <label for="contact">Are you willing to serve as a contact for the company you\'ve selected? </label><br>\r\n    <!--pass values of y=yes, n=no and m=maybe-->\r\n    <input id="contact" type="radio" name="contact" value="y">Yes<br>\r\n    <input id="contact" type="radio" name="contact" value="n">No<br>\r\n    <input id="contact" type="radio" name="contact" value="m">Maybe<br><br>\r\n\r\n    <label for="time_looking">How much time did you spend looking for your full-time position? </label><br> <!--list of possible job descriptions-->\r\n    <div class="dropdown">\r\n      <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Dropdown Example\r\n      <span class="caret"></span></button>\r\n      <ul class="dropdown-menu">\r\n')
        for item in models.TIME_RANGE:
            __M_writer('          <li>')
            __M_writer(str( item ))
            __M_writer('</li>\r\n')
        __M_writer('      </ul>\r\n    </div>\r\n    <br><br>\r\n\r\n    <label for="difficulties">What difficulties did you encounter in finding an internship/full-time position?</label><br>\r\n    <input id="difficulties" type="text" name="difficulties" value=""><br><br>\r\n\r\n    <label for="appointment">How many times did you meet with Reid?</label><br>\r\n    <input id="appointment" type="text" name="appointment" value=""><br><br><!--drop down list of numbers for appointments-->\r\n\r\n    <label for="help_rating">Please rate Reid\'s helpfulness in your search for an internship/full-time position.</label><br>\r\n    <p>Not helpful at all\r\n    <input id="help_rating" type="radio" name="help_rating" value="1">1\r\n    <input id="help_rating" type="radio" name="help_rating" value="2">2\r\n    <input id="help_rating" type="radio" name="help_rating" value="3">3\r\n    <input id="help_rating" type="radio" name="help_rating" value="4">4\r\n    <input id="help_rating" type="radio" name="help_rating" value="5">5\r\n    <input id="help_rating" type="radio" name="help_rating" value="6">6\r\n    <input id="help_rating" type="radio" name="help_rating" value="7">7\r\n    <input id="help_rating" type="radio" name="help_rating" value="8">8\r\n    <input id="help_rating" type="radio" name="help_rating" value="9">9\r\n    <input id="help_rating" type="radio" name="help_rating" value="10">10\r\n    Exteremely helpful</p>\r\n\r\n    <label for="suggestions">What suggestion would you give to Reid to help him improve?</label><br>\r\n    <input id="suggestions" type="text" name="suggestions" value=""><br><br>\r\n\r\n    <label for="suggestions">What suggestion would you give to Reid to help him improve?</label><br>\r\n    <input id="suggestions" type="text" name="suggestions" value=""><br><br>\r\n\r\n    <hr><br><br>\r\n\r\n    <h1>Program Information</h1>\r\n    <p>Please help us improve the program with your clear feedback.</p>\r\n\r\n    <label for="program_introduction">How did you learn about the Information Systems program?</label><br>\r\n    <div class="dropdown">\r\n      <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Dropdown Example\r\n      <span class="caret"></span></button>\r\n      <ul class="dropdown-menu">\r\n')
        for item in PROGRAM_INTRO:
            __M_writer('          <li>')
            __M_writer(str( item ))
            __M_writer('</li>\r\n')
        __M_writer('      </ul>\r\n    </div>\r\n    <br><br>\r\n\r\n    <label for="mism_decision">Why did you decide to pursue the MISM?</label><br>\r\n    <input id="mism_decision" type="text" name="mism_decision" value=""><br><br>\r\n\r\n    <label for="again">Given the opportunity to start over, would you choose IS again?</label><br>\r\n    <!--pass values of y=yes, n=no and ns=not sure-->\r\n    <input id="again" type="radio" name="again" value="y">Yes<br>\r\n    <input id="again" type="radio" name="again" value="n">No<br>\r\n    <input id="again" type="radio" name="again" value="ns">Not Sure<br><br>\r\n\r\n    <label for="again_response">Please explain your response to the question above.</label><br>\r\n    <input id="again_response" type="text" name="again_response" value=""><br><br>\r\n\r\n    <label for="additional_classes">What classes or topics would you have liked to take that were not offered?</label><br>\r\n    <input id="additional_classes" type="text" name="additional_classes" value=""><br><br>\r\n\r\n    <label for="valuable_class">What was the most valuable class in the MISM?</label><br>\r\n    <div class="dropdown">\r\n      <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Dropdown Example\r\n      <span class="caret"></span></button>\r\n      <ul class="dropdown-menu">\r\n')
        for item in PROGRAM_INTRO:
            __M_writer('          <li>')
            __M_writer(str( item ))
            __M_writer('</li>\r\n')
        __M_writer('      </ul>\r\n    </div>\r\n    <br><br>\r\n\r\n    <label for="valuable_class_response">Please explain your response to the question above.</label><br>\r\n    <input id="valuable_class_response" type="text" name="valuable_class_response" value=""><br><br>\r\n\r\n    <label for="best_response">What did you like best about the MISM and why?</label><br>\r\n    <input id="best_response" type="text" name="best_response" value=""><br><br>\r\n\r\n    <label for="recommendation">What recommendations would you make to improve the program? </label><br>\r\n    <input id="recommendation" type="text" name="recommendation" value=""><br><br>\r\n\r\n    <!--How do I distinguish this appointment from the Career Advisor appointment and so on?-->\r\n    <label for="appointment">How many times did you meet with Caroline?</label><br>\r\n    <input id="appointment" type="text" name="appointment" value=""><br><br><!--drop down list of numbers for appointments-->\r\n\r\n    <label for="help_rating">Please rate Caroline\'s helpfulness in your search for an internship/full-time position.</label><br>\r\n    <p>Not helpful at all\r\n    <input id="help_rating" type="radio" name="help_rating" value="1">1\r\n    <input id="help_rating" type="radio" name="help_rating" value="2">2\r\n    <input id="help_rating" type="radio" name="help_rating" value="3">3\r\n    <input id="help_rating" type="radio" name="help_rating" value="4">4\r\n    <input id="help_rating" type="radio" name="help_rating" value="5">5\r\n    <input id="help_rating" type="radio" name="help_rating" value="6">6\r\n    <input id="help_rating" type="radio" name="help_rating" value="7">7\r\n    <input id="help_rating" type="radio" name="help_rating" value="8">8\r\n    <input id="help_rating" type="radio" name="help_rating" value="9">9\r\n    <input id="help_rating" type="radio" name="help_rating" value="10">10\r\n    Exteremely helpful</p>\r\n\r\n    <label for="suggestions">What suggestion would you give to Caroline to help her improve?</label><br>\r\n    <input id="suggestions" type="text" name="suggestions" value=""><br><br>\r\n\r\n\r\n    <label for="give_back">When you are able to do so, will you give back to the Information Systems program?</label><br>\r\n    <input id="give_back" type="radio" name="give_back" value="1">Money (donations to department, scholarship funds, etc.)<br>\r\n    <input id="give_back" type="radio" name="give_back" value="2">Time (mentoriship, guest lectures, etc.)<br>\r\n    <input id="give_back" type="radio" name="give_back" value="3">Both<br>\r\n    <input id="give_back" type="radio" name="give_back" value="4">I don\'t plan on giving back<br><br>\r\n\r\n    <label for="my_choice">Did you participate in "My Choice to Give"?</label><br>\r\n    <input id="my_choice" type="radio" name="my_choice" value="yes">Yes<br>\r\n    <input id="my_choice" type="radio" name="my_choice" value="no">No<br>\r\n\r\n    <label for="additional_comments">Anything else you\'d like us to know?</label><br>\r\n    <input id="additional_comments" type="text" name="additional_comments" value=""><br><br>\r\n  </form>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/isys-sec/Documents/AlumniDb/alumni-webapp/surveys/templates/exit_survey.html", "uri": "exit_survey.html", "line_map": {"64": 83, "65": 83, "66": 85, "67": 109, "68": 110, "37": 1, "70": 110, "71": 112, "60": 40, "42": 160, "77": 71, "48": 4, "69": 110, "56": 4, "57": 39, "58": 40, "59": 40, "28": 0, "61": 42, "62": 82, "63": 83}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
