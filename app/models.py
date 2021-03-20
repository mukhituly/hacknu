import pickle
import numpy as np
import pandas as pd
import lightgbm
from xgboost import XGBClassifier


def breast_cancer_predict(mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness):
    X = np.array([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])
    model = pickle.load(open("weights/breast-cancer-92.pkl", 'rb'))
    result = model.predict(X)
    return int(result[0])


def stroke_predict(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status):
    # creating the pandas dataframe and replicating previous steps
    a_dict = {'gender': [int(gender)], 'age': [int(age)], 'hypertension': [int(hypertension)], 'heart_disease': [int(heart_disease)], 
           'ever_married': [int(ever_married)], 'work_type': [int(work_type)], 'Residence_type': [int(Residence_type)], 
           'avg_glucose_level': [float(avg_glucose_level)], 'bmi': [float(bmi)], 'smoking_status': [int(smoking_status)]}
    data = pd.DataFrame(a_dict)
    data['gender'] = 1 if gender == 'male' else 0
    data['ever_married'] = 1 if ever_married == 'Yes' else 0
    work_mapping = {'Self_employed': 3,'Private' : 2, 'children' : 1, 'Govt_job': 0}
    data['work_type'] = data['work_type'].map(work_mapping)
    data['Residence_type'] = 1 if Residence_type == 'Urban' else 0
    smoke_mapping = {'Unknown': 0, 'formerly smoked': 1, 'never_smoked': 2, 'smokes': 3}
    data['smoking_status'] = data['smoking_status'].map(smoke_mapping)
    # after data has been replicated
    xgb = XGBClassifier()
    xgb.load_model("weights/stroke.model")
    return xgb.predict(data)[0]