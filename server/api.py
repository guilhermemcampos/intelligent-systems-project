from flask import Flask
from flask import request
from flask import json
import pickle
import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return {"message" : "Hello!"}

@app.route("/v1/categorize", methods=["POST"])
def hellocategorize():
    test_products = request.json["products"]
    
    df = pd.DataFrame(test_products)
    titles = list(df['title'])
    
    MODEL_BAG_OF_WORDS_PATH  = os.environ['MODEL_BAG_OF_WORDS_PATH']
    model_bag_of_words = pickle.load(open(MODEL_BAG_OF_WORDS_PATH, 'rb'))

    MODEL_PATH  = os.environ['MODEL_PATH']
    model = pickle.load(open(MODEL_PATH, 'rb'))
    
    prediction = model.predict(model_bag_of_words.transform(titles))

    return json.jsonify({"categories":list(prediction)})

    
