from flask import Flask , render_template , request, flash
import joblib
import sys
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Get the logger
logger = logging.getLogger(__name__)

# Log the root path
logger.info("Root path: %s", app.root_path)


app.root_path = "/usr/app/src/model"

# Log the updated root path
logger.info("Updated root path: %s", app.root_path)

from sentify import SentimentAnalyzer

app.root_path = os.getcwd()

@app.route("/" , methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])        
def predict():
    if "tweet" not in request.form:
        return "Input a valid tweet"
    
    file = request.form["tweet"]    
    predicted = get_predictions(file)
    return render_template("index.html" , predicted = "Emotion: {}".format(predicted)  )

def get_predictions(tweet:str): 
    sys.path.append("./usr/app/src/")
    SentimentAnalyzer = joblib.load("./model/sentify.pkl")
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