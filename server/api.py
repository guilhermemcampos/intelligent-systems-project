from flask import Flask
from flask import request
from flask import json
from flask_expects_json import expects_json
import pickle
import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return {"message" : "Hello!"}

#Schema for products json validation
schema = {
    'type': 'object',
    'properties': {
        'products': {
            'type': 'array',
            'minItems': 1,
            
        },
    },
    'required': ['products']
}

def loadFeatureExtractionModel():
    MODEL_BAG_OF_WORDS_PATH  = os.environ['MODEL_BAG_OF_WORDS_PATH']
    return pickle.load(open(MODEL_BAG_OF_WORDS_PATH, 'rb'))

def loadCategorizationModel():
    MODEL_PATH  = os.environ['MODEL_PATH']
    return pickle.load(open(MODEL_PATH, 'rb'))

@app.route("/v1/categorize", methods=["POST"])
@expects_json(schema)
def categorize():
    products = request.json['products']
    
    feature_extraction_model = loadFeatureExtractionModel()
    categorization_model = loadCategorizationModel()
    
    df = pd.DataFrame(products)
    titles = list(df['title'])
    prediction = categorization_model.predict(feature_extraction_model.transform(titles))

    return json.jsonify({"categories":list(prediction)})
    

    
