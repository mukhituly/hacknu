from flask import render_template, flash, redirect, url_for
from app import app
from app.form import *

from app.models import *



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SurveyForm()

    if form.validate_on_submit():
        print(form.age.data, flush=True)

        flash()
        return redirect(url_for('index'))
    return render_template('survey.html', form=form)


@app.route("/breast_cancer", methods=["GET", "POST"])
def breast_cancer():
    form = BreastCancerForm()

    if form.validate_on_submit():
        print(form.mean_radius.data, flush=True)

        pred = breast_cancer_predict(form.mean_radius.data,
                                     form.mean_texture.data,
                                     form.mean_perimeter.data,
                                     form.mean_area.data,
                                     form.mean_smoothness.data) #17.99, 10.38, 122.80, 1001.0, 0.11840)

        if pred:
            flash("You have breast cancer :C")
        else:
            flash("You don't have breast cancer c:")
        return redirect(url_for('breast_cancer'))
    return render_template('breast_cancer.html', form=form)
