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
    # print(form.stroke_form.avg_glucose_level, flush=True)

    if form.breast_cancer_form.validate_on_submit():
        pred = breast_cancer_predict(
                            form.breast_cancer_form.mean_radius.data,
                            form.breast_cancer_form.mean_texture.data,
                            form.breast_cancer_form.mean_perimeter.data,
                            form.breast_cancer_form.mean_area.data,
                            form.breast_cancer_form.mean_smoothness.data) #17.99, 10.38, 122.80, 1001.0, 0.11840)

        if pred:
            flash("You have breast cancer :C")
        else:
            flash("You don't have breast cancer c:")

        return redirect(url_for('index'))

    if form.stroke_form.validate_on_submit():
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
            flash("You don't have stroke c:")

        return redirect(url_for('index'))

    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('survey.html', form=form)
