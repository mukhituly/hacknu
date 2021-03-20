from flask_wtf import FlaskForm
from wtforms import *
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.widgets import CheckboxInput, ListWidget


class SurveyForm(FlaskForm):

    age = IntegerField('Age')
    submit = SubmitField('Submit')


class HeartAttackForm(FlaskForm):

    age = IntegerField('Age')

    gender = RadioField('Gender', choices=[
        ('male', 'Male'),
        ('female', 'Female'),])

    path = SelectField(
        'Which web development path do you identify yourself with?',
        choices=[
            # ('', 'Select your path'),
            ('front', 'Front End'),
            ('back', 'Back End'),
            ('full', 'Full Stack'),
        ])

    language = SelectMultipleField(
        'What programming languages do you use?',
        choices=[
            ('js', 'JavaScript'),
            ('ts', 'TypeScript'),
            ('py', 'Python'),
            ('csharp', 'C#'),
            ('java', 'Java'),
            ('other', 'Other'),
        ],
        option_widget=CheckboxInput(),
        widget=ListWidget())

    text_area = TextAreaField('comments')

    submit = SubmitField('Submit')


class BreastCancerForm(FlaskForm):
    mean_radius = FloatField("Mean Radius of Nipple")
    mean_texture = FloatField("Mean Texture of Nipple")
    mean_perimeter = FloatField("Mean Perimeter of Nipple")
    mean_area = FloatField("Mean Area of Nipple")
    mean_smoothness = FloatField("Mean Smoothness")

    submit = SubmitField("Submit")