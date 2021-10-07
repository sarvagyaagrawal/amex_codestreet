from sklearn import preprocessing
from imblearn.over_sampling import RandomOverSampler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,roc_auc_score,cohen_kappa_score,confusion_matrix,roc_curve,balanced_accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from django.forms.models import model_to_dict

import pickle
from .utils import *
import pandas as pd
import numpy as np

def linear_regression(amt1,amt2,amt3,amt4):
    pipe=pickle.load(open("customer/linear_regression_model.sav", "rb"))
    pred=pipe.predict([[amt1,amt2,amt3,amt4]])
    result=pred.tolist()
    return result[0]

def calc_future_spendings_linear_regress(amt1,amt2,amt3,amt4):
    monthly_spend=linear_regression(amt1,amt2,amt3,amt4)
    tota_6_month_spend=monthly_spend*6
    return tota_6_month_spend,monthly_spend

def monthly_pred_saving(monthly_pred_spend,income):
    if income-monthly_pred_spend>0:
        return income-monthly_pred_spend
    else:
        return 0
