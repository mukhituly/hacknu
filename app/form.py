from flask_wtf import FlaskForm
from wtforms import *
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.widgets import CheckboxInput, ListWidget


class SurveyForm(FlaskForm):
    age = IntegerField("Age")
    gender = RadioField("Gender", choices=[
        (0,"Male"),
        (1,"Female"),
        (2,"Other"),
    ])

    submit = SubmitField("Submit")


class BreastCancerForm(FlaskForm):
    mean_radius = FloatField("Mean Radius of Nipple")
    mean_texture = FloatField("Mean Texture of Nipple")
    mean_perimeter = FloatField("Mean Perimeter of Nipple")
    mean_area = FloatField("Mean Area of Nipple")
    mean_smoothness = FloatField("Mean Smoothness")


class StrokeForm(FlaskForm):
    hypertension = RadioField("Hypertension", choices=[
        (0,"I don't have hypertension"),
        (1,"I have hypertension"),
    ])
    heart_disease = RadioField("Heart Disease", choices=[
        (0,"I don't have any heart diseases"),
        (1,"I have heart disease"),
    ])
    ever_married = RadioField("Married or was Married?", choices=[
        (0,"No"),
        (1,"Yes"),
    ])
    work_type = RadioField("Work Type", choices=[
        (0,"I don't work, I have children"),
        (1,"Government job"),
        (2,"Never worked"),
        (3,"Private job"),
        (4,"Self-employed"),
    ])
    residence_type = RadioField("Residence Type?", choices=[
        (0,"Rural"),
        (1,"Urban"),
    ])

    avg_glucose_level = FloatField("Average Glucose Level")
    bmi = FloatField("Body Mass Index")

    smoking_status = RadioField("Do you smoke?", choices=[
        (0,"I stopped smoking"),
        (1,"Never smoked"),
        (2,"Yes"),
    ])