import pickle
import numpy as np
import pandas as pd
import lightgbm


def breast_cancer_predict(mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness):
    X = np.array([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])
    model = pickle.load(open("weights/breast-cancer-92.pkl", 'rb'))
    result = model.predict(X)
    return int(result[0])