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


def heart_attack_predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    """
        * Age (age in years)
        * Sex (1 = male; 0 = female)
        * CP (chest pain type) (typical angina, atypical angina, non-anginal pain, asymptomatic)
        * TRESTBPS (resting blood pressure (in mm Hg on admission to the hospital))
        * CHOL (serum cholesterol in mg/dl)
        * FBS (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
        * RESTEGC (resting electrocardiographic results)
        * THALACH (maximum heart rate achieved)
        * EXANG (exercise induced angina (1 = yes; 0 = no))
        * OLDPEAK (ST depression induced by exercise relative to rest)
        * SLOPE (the slope of the peak exercise ST segment)
        * CA (number of major vessels (0-3) colored by flourosopy)
        * THAL (3 = normal; 6 = fixed defect; 7 = reversable defect)
        * RESULT (1 or 0)
    """

    X = np.array([[int(age),
                   int(sex),
                   int(cp),
                   float(trestbps),
                   float(chol),
                   int(fbs),
                   int(restecg),
                   int(thalach),
                   int(exang), 
                   float(oldpeak),
                   int(slope),
                   int(ca),
                   int(thal)
                ]])
    model = pickle.load(open("weights/heart-attack-95.pkl", 'rb'))
    scaler = pickle.load(open("weights/heart-attack-scaler.bin", 'rb'))
    X_scaled = scaler.transform(X)
    result = model.predict(X_scaled)
    return result[0]


def diabetes_predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    """
        * Pregnancies: Number of times pregnant
        * Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
        * BloodPressure: Diastolic blood pressure (mm Hg)
        * SkinThickness: Triceps skin fold thickness (mm)
        * Insulin: 2-Hour serum insulin (mu U/ml)
        * BMI: Body mass index (weight in kg/(height in m)^2)
        * DiabetesPedigreeFunction: Diabetes pedigree function
        * Age: Age (years)
    """
    X = np.array([[int(Pregnancies),
                   int(Glucose),
                   int(BloodPressure),
                   int(SkinThickness),
                   int(Insulin),
                   float(BMI),
                   float(DiabetesPedigreeFunction),
                   int(Age)
                ]])
    model = pickle.load(open("weights/diabetes-87.pkl", 'rb'))
    scaler = pickle.load(open("weights/diabetes.bin", 'rb'))
    X_scaled = scaler.transform(X)
    print(X_scaled)
    result = model.predict(X_scaled)
    return result[0]


def liver_disease_predict(Age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio, Gender):
    """
        * Age Age of the patient
        * Total_Bilirubin Total Bilirubin
        * Direct_Bilirubin Direct Bilirubin
        * Alkaline_Phosphotase Alkaline Phosphotase
        * Alamine_Aminotransferase Alamine Aminotransferase
        * Aspartate_Aminotransferase Aspartate Aminotransferase
        * Total_Protiens Total Protiens
        * Albumin Albumin
        * Albumin_and_Globulin_Ratio Albumin and Globulin Ratio
        * Gender Gender of the patient
    """

    X1 = np.array([[int(Age),
                    float(Total_Bilirubin),
                    float(Direct_Bilirubin),
                    int(Alkaline_Phosphotase),
                    int(Alamine_Aminotransferase),
                    int(Aspartate_Aminotransferase),
                    float(Total_Protiens),
                    float(Albumin),
                    float(Albumin_and_Globulin_Ratio)]])
    X2 = np.array([[int(Gender)]])
    model = pickle.load(open("weights/liver-disease-70.pkl", 'rb'))
    scaler = pickle.load(open("weights/liver-disease-scaler.bin", 'rb'))
    X1 = scaler.transform(X1)

    X = np.hstack((X1, X2))
    result = model.predict(X)
    return result[0]