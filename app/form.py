from flask_wtf import FlaskForm
from wtforms import *
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.widgets import CheckboxInput, ListWidget


class SurveyForm(FlaskForm):
    age = IntegerField("Age")
    submit = SubmitField("Submit")


class BreastCancerForm(FlaskForm):
    mean_radius = FloatField("Mean Radius of Nipple")
    mean_texture = FloatField("Mean Texture of Nipple")
    mean_perimeter = FloatField("Mean Perimeter of Nipple")
    mean_area = FloatField("Mean Area of Nipple")
    mean_smoothness = FloatField("Mean Smoothness")
