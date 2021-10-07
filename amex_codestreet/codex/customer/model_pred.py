from rest_framework.serializers import Serializer
# from rest_framework import serializers

from .serializers import CustomerSerializers, present_bankingSerializers,future_bankingSerializers
from .utils import *
from .models import Customer_details, present_banking, future_banking 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import pandas as pd
import numpy as np
import json
from django.core.serializers import serialize
from django.core import serializers

from sklearn import preprocessing
from imblearn.over_sampling import RandomOverSampler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,roc_auc_score,cohen_kappa_score,confusion_matrix,roc_curve,balanced_accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from django.forms.models import model_to_dict

import pickle
from django.core.serializers.json import DjangoJSONEncoder

# class LazyEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, json):
#             return str(obj)
#         return super().default(obj)
# class Customer_ModelSerializers(serializers.Serializer):
#     class Meta:
#         model=Customer_details
#         fields ="__all__"
        
# class Current_ModelSerializers(serializers.Serializer):
#     class Meta:
#         model=present_banking
#         fields ="__all__"

# class Future_ModelSerializers(serializers.Serializer):
#     class Meta:
#         model=future_banking
#         fields ="__all__"
def obj_to_dict(model_instance):
    serial_obj = serializers.serialize('json', [model_instance])
    obj_as_dict = json.loads(serial_obj)[0]['fields']
    obj_as_dict['pk'] = model_instance.pk
    return obj_as_dict

def getData(request):
    cust_det=Customer_details.objects.get(user=request.user)
    finance=present_banking.objects.get(user=request.user)
    future=future_banking.objects.filter(user=request.user)

    # serializer1=Customer_ModelSerializers(cust_det)
    # serializer2=Current_ModelSerializers(finance)
    # serializer3=Future_ModelSerializers(future)

    # content1 = JSONRenderer().render(serializer1.data)
    # content2 = JSONRenderer().render(serializer2.data)
    # content3 = JSONRenderer().render(serializer3.data)
    # serializer1=serialize('json', cust_det,cls=LazyEncoder)
    # serializer2=serialize('json',finance)
    # serializer3=serialize('json', future, cls=LazyEncoder)

    # return content1,content2, content3
    # return serializer1,serializer2,serializer3
    # inst=finance.__dict__
    # return inst
    return obj_to_dict(finance)

def getPredictions(curr):
    '''
        Parameters accepted:
            cust_det: serialized data {key:value} of model Customer_details of a user 
            curr_fin:  serialized data {key:value} of model present_banking of a user 
            fut_fin:  serialized data {key:value} of model future_banking of a user 
        
        This function will be used for calculation of Risk factor
    '''
    #collection of paramters for model testing
    # curr= json.loads(curr1)[0]['fields']
    # curr= json.loads(cust_det)
    # curr= json.loads(fut_fin)
    print("/n cuur serailzer print:",curr)
    tot_inc=return_income(float(curr["b_income_fut"]))
    tot_debt=return_debt(float(curr['b_due_amt_fut']))
    debt_to_inc=float(curr['b_debt_to_inc'])
    tot_saving=float(curr['b_total_savings'])
    spending_to_saving=float(curr['b_spend_to_save'])

    #model unpacking begins from here
    pipe=pickle.load(open("customer/final_model.sav", "rb"))
    # scaler = pipe.preprocessing.MinMaxScaler()
    # scaler.clip = False

    pred=pipe.predict_proba([[tot_inc,debt_to_inc,spending_to_saving,tot_saving]])
    result=pred.tolist()
    return "{:.2f}".format(result[0][1])


    