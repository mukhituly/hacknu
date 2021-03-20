from flask import render_template, flash, redirect, url_for
from app import app
from app.form import *

from app.models import *



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    form.breast_cancer_form = BreastCancerForm()
    print(form.csrf_token.label, flush=True)

    if form.breast_cancer_form.validate_on_submit():
        breast_cancer_pred = breast_cancer_predict(
                                    form.breast_cancer_form.mean_radius.data,
                                    form.breast_cancer_form.mean_texture.data,
                                    form.breast_cancer_form.mean_perimeter.data,
                                    form.breast_cancer_form.mean_area.data,
                                    form.breast_cancer_form.mean_smoothness.data) #17.99, 10.38, 122.80, 1001.0, 0.11840)

        if breast_cancer_pred:
            flash("You have breast cancer :C")
        else:
            flash("You don't have breast cancer c:")

        return redirect(url_for('index'))

    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('survey.html', form=form)
