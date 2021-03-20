from flask import render_template, flash, redirect, url_for
from app import app
from app.form import *

from app.models import *



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    form.breast_cancer_form = BreastCancerForm()
    form.stroke_form = StrokeForm()
    form.heart_attack_form = HeartAttackForm()
    form.diabetes_form = DiabetesForm()
    form.liver_disease_form = LiverDiseasePredict()
    # print(form.stroke_form.avg_glucose_level, flush=True)

    if form.breast_cancer_form.mean_radius.data is not None:
        pred = breast_cancer_predict(
                            form.breast_cancer_form.mean_radius.data,
                            form.breast_cancer_form.mean_texture.data,
                            form.breast_cancer_form.mean_perimeter.data,
                            form.breast_cancer_form.mean_area.data,
                            form.breast_cancer_form.mean_smoothness.data) #17.99, 10.38, 122.80, 1001.0, 0.11840)
        print(pred)
        if pred:
            flash("You have breast cancer :C")
        else:
            flash("You don't have breast cancer :)")

        return redirect(url_for('index'))

    if form.stroke_form.hypertension.data is not None:
        pred = stroke_predict(form.gender.data,
                              form.age.data,
                              form.stroke_form.hypertension.data,
                              form.stroke_form.heart_disease.data,
                              form.stroke_form.ever_married.data,
                              form.stroke_form.work_type.data,
                              form.stroke_form.residence_type.data,
                              form.stroke_form.avg_glucose_level.data,
                              form.stroke_form.bmi.data,
                              form.stroke_form.smoking_status.data)
        print(pred)
        if pred:
            flash("You have stroke :C")
        else:
            flash("You don't have stroke :)")

        return redirect(url_for('index'))

    if form.heart_attack_form.cp.data is not None:
        pred = heart_attack_predict(form.age.data,
                                    form.gender.data,
                                    form.heart_attack_form.cp.data,
                                    form.heart_attack_form.trestbps.data,
                                    form.heart_attack_form.chol.data,
                                    form.heart_attack_form.fbs.data,
                                    form.heart_attack_form.restecg.data,
                                    form.heart_attack_form.thalach.data,
                                    form.heart_attack_form.exang.data,
                                    form.heart_attack_form.oldpeak.data,
                                    form.heart_attack_form.slope.data,
                                    form.heart_attack_form.ca.data,
                                    form.heart_attack_form.thal.data)
        print(pred)
        if pred:
            flash("You have heart attack possibility :C")
        else:
            flash("You don't have heart attack possibility :)")
        return redirect(url_for('index'))

    if form.diabetes_form.Pregnancies.data is not None:
        pred = diabetes_predict(form.diabetes_form.Pregnancies.data,
                                form.diabetes_form.Glucose.data,
                                form.diabetes_form.BloodPressure.data,
                                form.diabetes_form.SkinThickness.data,
                                form.diabetes_form.Insulin.data,
                                form.diabetes_form.BMI.data,
                                form.diabetes_form.DiabetesPedigreeFunction.data,
                                form.age.data)
        print(pred)
        if pred:
            flash("You have diabetes :C")
        else:
            flash("You don't have diabetes :)")
        return redirect(url_for('index'))

    if form.liver_disease_form.Total_Bilirubin.data is not None:
        pred = liver_disease_predict(form.age.data,
                                    form.liver_disease_form.Total_Bilirubin.data,
                                    form.liver_disease_form.Direct_Bilirubin.data,
                                    form.liver_disease_form.Alkaline_Phosphotase.data,
                                    form.liver_disease_form.Alamine_Aminotransferase.data,
                                    form.liver_disease_form.Aspartate_Aminotransferase.data,
                                    form.liver_disease_form.Total_Protiens.data,
                                    form.liver_disease_form.Albumin.data,
                                    form.liver_disease_form.Albumin_and_Globulin_Ratio.data,
                                    form.gender.data)
        print(pred)
        if pred:
            flash("You have liver disease :C")
        else:
            flash("You don't have liver disease :)")
        return redirect(url_for('index'))

    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
