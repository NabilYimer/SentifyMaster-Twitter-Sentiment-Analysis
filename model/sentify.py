# Importing  necessary libraries

from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
from collections import Counter

import string
import nltk
import spacy

import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd 
pd.set_option('display.max_colwidth', None)



nlp = spacy.load("en_core_web_sm")  # download the english model
nltk.download('stopwords')          # download common stopwords from nltk

class SentimentAnalyzer():
    
    def __init__(self):
        self.vectorizer = CountVectorizer(ngram_range=(1,3))
        
        self.model = SVC(kernel='linear')
        
        self.smote = SMOTE(random_state = 42 ,sampling_strategy='minority')

        
    def pre_process(self,text):
        nlp = spacy.load("en_core_web_sm")
        tokens = nlp(text)
        
        # lemmatize

        tokens = [token.lemma_ for token in tokens]

        # remove stopwords and punctuations
                                                                                       # including targeted person and negation   
        stopwords_ = [word for word in nltk.corpus.stopwords.words('english') if word not in ['he', 'she','no', 'not', 'they', 'you']]

        tokens = [token for token in tokens if not token in string.punctuation and not token in stopwords_]                                            

        return ' '.join(tokens)



    def train(self,X_train,y_train):
        
        # vectorizing preprocessed text
        
        train = [self.pre_process(txt) for txt in X_train]
        
        train_vector = self.vectorizer.fit_transform(train)
        
        # handling the imbalanced labels
        X_train_smote,y_train_smote = self.smote.fit_resample(train_vector.astype('float'),y_train)

        # fitting the SVM
        self.model.fit(X_train_smote,y_train_smote)
        


    def predict(self,X_test):
        
        # pre-process by itrating over the df or if it is a single tweet 
        test = [self.pre_process(txt) for txt in X_test] if not isinstance(X_test,str) else [self.pre_process(X_test)]
        test_vector = self.vectorizer.transform(test)
        
        yhat_test = self.model.predict(test_vector)
        
        return yhat_test