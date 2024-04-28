from flask import Flask , render_template , request
import joblib
import sys
import os


app = Flask(__name__)

sys.path.append("./model/")
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
    return render_template("index.html" , predicted = "Emotion: {}".format(predicted)  )

def get_predictions(tweet:str): 
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
    # app.run(host="0.0.0.0",port="5000")
    app.run(debug=True)