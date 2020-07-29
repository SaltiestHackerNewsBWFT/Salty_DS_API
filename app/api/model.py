# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:07:08 2020

@author: Ronin
"""

import pandas as pd

from nltk.tokenize import RegexpTokenizer

from nltk.stem import WordNetLemmatizer,PorterStemmer

from nltk.corpus import stopwords

import json

import urllib

import re

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

lemmatizer = WordNetLemmatizer()

stemmer = PorterStemmer()

def get_compund_score(text):
        score = analyzer.polarity_scores(text)
        str(text)
        return score['compound']
    
def preprocess(sentence):
    sentence=str(sentence)
    sentence = sentence.lower()
    sentence=sentence.replace('{html}',"") 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', sentence)
    rem_url=re.sub(r'http\S+', '',cleantext)
    rem_num = re.sub('[0-9]+', '', rem_url)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(rem_num)  
    filtered_words = [w for w in tokens if len(
        w) > 2 if not w in stopwords.words('english')]
    #stem_words=[stemmer.stem(w) for w in filtered_words]
    #lemma_words=[lemmatizer.lemmatize(w) for w in stem_words]
    return " ".join(filtered_words)

def func(id):
  x=[]
  html = urllib.request.urlopen(
      'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json')
  x.append(json.loads(html.read()))
  df = pd.DataFrame.from_dict(x)
  print(df.head())
  df_comments = df[df['type'] == 'comment']
  df_comments['clean_text']= df_comments['text'].map(lambda s:preprocess(s)) 
  df_comments['clean_vader_score'] =   df_comments['clean_text'].apply(
      get_compund_score)
  
  return (df_comments['clean_vader_score'][0])