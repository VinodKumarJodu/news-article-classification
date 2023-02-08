import os, sys
import numpy as np 
import pandas as pd 

import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet

dir = '/home/v/news-article-classification/news/nltk_data'
nltk.download('stopwords', download_dir=dir)
nltk.download('wordnet', download_dir=dir)
nltk.download('punkt', download_dir=dir)
nltk.download('averaged_perceptron_tagger',download_dir=dir)

import warnings
warnings.filterwarnings('ignore')

from news.logger import logging
from news.exception import NewsException

from news.entity.config_entity import DataTransformationConfig
from news.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact

class DataTransformation:
    def __init__(self, data_validation_artifact:DataValidationArtifact,data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config    

            self.add_words = ["mr","also","would","could","say","u"]
            self.stop_words = set(stopwords.words("english"))
            self.stop_added = self.stop_words.union(self.add_words)        
        except Exception as e:
            raise NewsException(e, sys)

    @staticmethod
    def read_data(file_path)-> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NewsException(e, sys)
    
    def clean_text(self, text):
        try:
            text = " ".join([x.lower() for x in text.split()])
            text = re.sub(r'\(.*?\)', '', text)
            text = re.sub(r'\[.*?\]', '', text)
            text = re.sub(r'[%s]' %re.escape(string.punctuation),'', text)
            text = re.sub(r'[^a-zA-z]?\w*\d\w','', text)
            text = re.sub(r'\S*https?:\S*','', text)
            text = re.sub(r'<.*?>','', text)
            text = re.sub(r'\n',' ', text)
            text = re.sub("[''""...“”‘’…]", '', text)
            text = ' '.join([text for text in text.split() if text not in self.stop_added])
            text = re.compile("["
                                    u"\U0001F600-\U0001F64F"  # emoticons
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                    u"\U00002500-\U00002BEF"  # chinese char
                                    u"\U00002702-\U000027B0"
                                    u"\U00002702-\U000027B0"
                                    u"\U000024C2-\U0001F251"
                                    u"\U0001f926-\U0001f937"
                                    u"\U00010000-\U0010ffff"
                                    u"\u2640-\u2642"
                                    u"\u2600-\u2B55"
                                    u"\u200d"
                                    u"\u23cf"
                                    u"\u23e9"
                                    u"\u231a"
                                    u"\ufe0f"  # dingbats
                                    u"\u3030"
                                    "]+", flags=re.UNICODE).sub(r'', text) #emojis and symbols
            text = text.strip()
            text = ' '.join([text.strip() for text in text.split()])
            return text
        except Exception as e:
            raise NewsException(e, sys)
    
    def get_wordnet_pos(self, tag):
    # Map POS tag to first character used by wordnet.lemmatize()
    tag = tag[0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

    def lemmatize_with_pos(self, text):
        tokens = word_tokenize(text)
        # POS tag tokens
        tagged_tokens = nltk.pos_tag(tokens)
        # Create lemmatizer object
        lemmatizer = WordNetLemmatizer()
        # Lemmatize each token with POS tag
        lemmatized_tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(tag)) for token, tag in tagged_tokens]
        # Join lemmatized tokens back into text
        lemmatized_text = " ".join([token for token in lemmatized_tokens if token not in stop_added])
        return lemmatized_text

    def remove_stopwords_after_pos(self, text):
        try:
            text = ' '.join([text for text in text.split() if text not in stop_added])
            return text
        except Exception as e:
            raise NewsException(e, sys)

    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
            
            train_df['Text'] = train_df['Text'].apply(lambda x: self.clean_text(x))
            test_df['Text'] = test_df['Text'].apply(lambda x: self.clean_text(x))

            train_df['Text'] = train_df['Text'].apply(lambda x: self.lemmatize_with_pos(x))
            test_df['Text'] = test_df['Text'].apply(lambda x: self.lemmatize_with_pos(x))

            train_df['Text'] = train_df['Text'].apply(lambda x: self.remove_stopwords_after_pos(x))
            test_df['Text'] = test_df['Text'].apply(lambda x: self.remove_stopwords_after_pos(x))

            data_transformation_artifact = DataTransformationArtifact(transformed_object_file_path='None',
                                                                    transformed_train_file_path='None',
                                                                    transformed_test_file_path='None')
            return data_transformation_artifact
        except Exception as e:
            raise NewsException(e, sys)
