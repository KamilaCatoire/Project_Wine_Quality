# app.py

import uvicorn
import json
import pandas as pd 
from pydantic import BaseModel
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile

from fastapi import FastAPI
import pickle 
from sklearn.linear_model import LinearRegression, LogisticRegression
import numpy as np
from pydantic import BaseModel
from keras.models import load_model
import tensorflow as tf
import joblib
from typing import List
import requests

file = open("mon_modele4.h5",'rb')
model = load_model('mon_modele4.h5')
file.close()

# Load  model                                                                            
# file = open("v5_random_forest_class_bin_rw_ww.pkl",'rb')
# model = pickle.load(file)
# file.close()

with open('explainer', 'rb') as f: explainer = dill.load(f)
data = pd.read_csv('wines.csv', sep=',')

# 2. Classe qui représente la requête 
class Requests(BaseModel):
    fixed_acidity : Union [int, float]
    volatile_acidity: Union [int, float]
    citric_acid: Union [int, float]
    residual_sugar : Union [int, float]
    chlorides : Union [int, float]
    free_sulfur_dioxide : Union [int, float]
    total_sulfur_dioxide :Union [int, float]
    density :Union [int, float]
    pH :Union [int, float]
    sulphates : Union [int, float]
    alcohol : Union [int, float]
    type : Union [int, float]

# data = {'fixed acidity': 'fixed_acidity',
#         'volatile acidity': 'volatile_acidity',
#         'citric acid': 'citric_acid',
#         'residual sugar': 'residual_sugar',
#         'chlorides': 'chlorides',
#         'free sulfur dioxide': 'free_sulfur_dioxide',
#         'total sulfur dioxide':'total_sulfur_dioxide',
#         'density': 'density',
#         'pH': 'pH',
#         'alcohol':'alcohol',
#         'sulphates':'sulphates',
#         'type': [0 if 'wine_type' == 'white' else 1]}

# r = requests.post("http://localhost:4100/WineQuality", json = data)
    
# print (r.text)

def predict_quality(features_dict):
   features_array = np.array(list(features_dict.values())).reshape(1,-1)
   print(features_dict)
   print(features_array)
   quality_score = model.predict(features_array)

   return quality_score

#test_features = [0,0,0,0,0,0,0,0,0,0,0]

app = FastAPI()
@app.get("/")
async def root():
 return {"Wine Quality":"Welcome! Make your choice based on the quality!"}

@app.post("/WineQuality")
async def choose_wine_quality(input_requests: Requests): 
    #test_features = input_requests.features
    test_features = {'fixed acidity': input_requests.fixed_acidity, 
    'volatile acidity':input_requests.volatile_acidity, 
    'citric_acid':input_requests.citric_acid, 
    'residual_sugar':input_requests.residual_sugar,
    'chlorides':input_requests.chlorides, 
    'free_sulfur_dioxide':input_requests.free_sulfur_dioxide, 
    'total_sulfur_dioxide':input_requests.total_sulfur_dioxide, 
    'density':input_requests.density, 
    'pH':input_requests.pH, 
    'sulphates':input_requests.sulphates, 
    'alcohol':input_requests.alcohol,
    'type':input_requests.type}
   
    score = predict_quality(test_features)
    exp = explainer.explain_instance(
    data_row=data_row[0], 
    predict_fn= 
 )

    return {"score":score.tolist()}

