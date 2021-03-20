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


class HeartAttackForm(FlaskForm):
    cp = RadioField("Married or was Married?", choices=[
        (0, "Typical Angina"),
        (1, "Atypical Angina"),
        (2, "non-anginal pain"),
        (3, "asymptomatic")
    ])
    trestbps = FloatField("Resting Blood Pressure (mm/Hg)")
    chol = FloatField("Serum Cholesterol (mg/dL)")
    fbs = RadioField("Is Fasting Blood Sugar Level > 120 mg/dL?", choices=[
        (0, "No"), (1, "Yes")
    ])
    restecg = RadioField("Resting Electrocardiographic Results?", choices=[
        (0, "Normal"),
        (1, "Has ST-T wave abnormality"),
        (2, "Shows Probability or Definite Left Ventricular Hypertrophy")
    ])
    thalach = IntegerField("Maximum heart Rate Achieved")
    exang = RadioField("Exercise Induced Angina?", choices=[
        (0, "No"), (1, "Yes")
    ])
    oldpeak = IntegerField("ST depression induced by exercise relative to rest")
    slope = IntegerField("the slope of the peak exercise ST segment")
    ca = IntegerField("number of major vessels (0-3) colored by flourosopy")
    thal = IntegerField("Thal")


class DiabetesForm(FlaskForm):
    Pregnancies=IntegerField("Number of times pregnant")
    Glucose=IntegerField("Plasma glucose concentration a 2 hours in an oral glucose tolerance test")
    BloodPressure=IntegerField("Diastolic blood pressure (mm/Hg)")
    SkinThickness=IntegerField("Triceps skin fold thickness (mm)")
    Insulin=IntegerField("2-Hour serum insulin (mu U/ml)")
    BMI=FloatField("Body mass index (weight in kg/(height in m)^2)")
    DiabetesPedigreeFunction=FloatField("Diabetes pedigree function")


class LiverDiseasePredict(FlaskForm):
    Total_Bilirubin=FloatField("Total Bilirubin (mg/dL)")
    Direct_Bilirubin=FloatField("Conjugated Bilirubin (mg/dL)")
    Alkaline_Phosphotase=IntegerField("ALP (IU/L)")
    Alamine_Aminotransferase=IntegerField("ALT (IU/L)")
    Aspartate_Aminotransferase=IntegerField("AST (IU/L)")
    Total_Protiens=FloatField("Total Proteins (g/dL)")
    Albumin=FloatField("Albumin (g/dL)")
    Albumin_and_Globulin_Ratio=FloatField("A/G Ratio")
