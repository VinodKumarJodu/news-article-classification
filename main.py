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

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import log_loss
from sklearn.pipeline import Pipeline

import joblib

import warnings
warnings.filterwarnings('ignore')
nltk.download('stopwords')

stop = stopwords.words('english')

def preprocess(text):
    # text to lower case
    text = " ".join([word.lower() for word in text.split()])

    # remove url
    text = re.sub(r"\S*https?:\S*",'',text)

    # remove html tags
    text = re.sub(r"<.*?>",'',text)

    # remove punctuations
    text = re.sub('[%s]' %re.escape(string.punctuation), '', text)

    #remove new line character
    text = re.sub(r'\n','',text)

    # remove stopwords
    text = " ".join([word for word in text.split() if word not in stopwords.words('english')])

    return text


def model_training(train, model):
    X_train, X_test, y_train, y_test = train_test_split(train)