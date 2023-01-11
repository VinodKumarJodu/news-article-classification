import os
import string
import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt 
import seaborn as sns

import re
import nltk
from wordcloud import WordCloud 
from textblob import TextBlob 
from nltk.corpus import wordnet, stopwords 
from nltk.stem import WordNetLemmatizer
from gensim.models import word2vec
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import log_loss, confusion_matrix, accuracy
from sklearn.pipeline import Pipeline

import joblib

import warnings
warnings.filterwarnings('ignore')
# nltk.download('stopwords')

stop = stopwords.words('english')

path = '/config/workspace/source/train/train.csv'
def read_data(path):
    df = pd.read_csv(path, names=['articleid', 'text', 'category'])
    # df.columns = [column.lower() for column in df.columns]
    return df

def preprocess(text):
    text = " ".join([word.lower() for word in text.split()])
    text = re.sub(r"\S*https?:\S*",'',text)
    text = re.sub(r"<.*?>",'',text)
    text = re.sub('[%s]' %re.escape(string.punctuation), '', text)
    text = re.sub(r'\n','',text)
    text = " ".join([word for word in text.split() if word not in stopwords.words('english')])
    return text

def split_data(X,y):
    # df.columns = [column.lower() for column in df.columns]
    X = df['text']
    y = df['category']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=19)
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    return X_train, X_test, y_train, y_test

def label_encode(y_train,y_test):
    le = LabelEncoder()
    y_train = le.fit_transform(y_train)
    y_test = le.transform(y_test)
    return y_train, y_test

def model_training(X_train,y_train, X_test, y_test):
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return log_loss(y_test.values, y_pred)

if __name__ == "__main__":
    df = read_data(path)
    print(df.columns)
    df['text'] = df['text'].apply(lambda x:preprocess(x))
    X = df['text']
    y = df['category']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=19, stratify=True)
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train = vectorize.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    le = LabelEncoder()
    y_train = le.fit_transform(y_train)
    y_test = le.transitionType(y_test)
    model = MultinomialNB()
    model = model.fit(X_train.to_array(),y_train.values)
    y_pred = model.predict(X_test)
    loss = log_loss(y_test,y_pred)
    print(loss)
