# coursecombine/forms.py

from wtforms import Form
from wtforms import SelectField, SelectMultipleField, widgets, RadioField, TextField, validators
from datetime import date


class SelectCoursesForm(Form):
    courseIds = SelectMultipleField("Which courses would you like combined into a single course in D2L?", 
        description="Select as many course sections as you want combined into one.",
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        validators=[validators.Required(message="You must select at least two courses to combine")])
    baseCourse = RadioField('Which course do you want the others added to?',
        description="Select the course in which you are or will be developing" +\
            " your course content and materials so that these changes will be" +\
            " kept after the combination is complete.",
        validators=[validators.Required(message="You must select a course")])

class AdditionalCourseForm(Form):
    classNumber = TextField('Class Number', validators=[validators.Required(message="Class number is required."),
        validators.Regexp(regex=r'\d{5}', message="Please double check the class number.")])
    sessionLength = SelectField('Session Length',
        default='14W',
        validators=[validators.required()],
        choices=[
            ('8W', 'Eight Week'),
            ('4W1', 'Four Week - First'),
            ('4W2', 'Four Week - Second'),
            ('14W', 'Fourteen Week'),
            ('7W1', 'Seven Week - First'),
            ('7W2', 'Seven Week - Second'),
            ('17W', 'Seventeen Week'),
            ('10W', 'Ten Week'),
            ('3WI', 'Three Week Interim')
            ])
    subject = TextField('Subject Code', validators=[validators.Required(message="Subject code is required."),
        validators.Regexp(regex=r'[a-zA-Z ]{3,8}', message="Please double check the subject.")])
    catalogNumber = TextField('Catalog Number', validators=[validators.Required(message="Catalog Number is required."),
        validators.Regexp(regex=r'\d{3}', message="Please double check the catalog number.")])
    section = TextField('First 4-digits of section', validators=[validators.Required(message="Section is required."),
        validators.Regexp(regex=r'\d{3}[a-zA-Z]{1}', message="Please double check the section.")])