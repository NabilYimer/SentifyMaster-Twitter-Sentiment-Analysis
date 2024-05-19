from flask import Flask , render_template , request, flash
import joblib
import sys
import os
import logging

app = Flask(__name__)


# Append the model directory to the system path
sys.path.append(os.path.join(app.root_path, '../model'))

# Import the SentimentAnalyzer class from sentify module
from sentify import SentimentAnalyzer


@app.route("/" , methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])        
def predict(): 
    if "tweet" not in request.form:
        return "Input a valid tweet"
    
    file = request.form["tweet"]    
    predicted = get_predictions(file)
    return render_template("index.html" , predict = "Emotion: {}".format(predicted)  )

def get_predictions(tweet:str): 
    model_path = os.path.join(app.root_path, '../model/sentify.pkl')
    SentimentAnalyzer = joblib.load(model_path)
    result = SentimentAnalyzer.predict(tweet)[0]
    
    emotions = { 
    
    0 :'Sadness 😢'   ,
    1 :'Joy 🤩'       ,
    2 : 'Love ❤️'    ,
    3 : 'Anger 😠 '    ,
    4 :  'Fear 😨'    ,
    5 : 'Surprise 😮'
    
        }
    
    emotions = emotions[result]
    
    
    
    return emotions

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)  # for deployment
    # app.run(debug=True)   # for testing