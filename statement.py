import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import re

df = pd.read_csv('statement.CSV')
df = df.drop(['Memo'],axis=1)
lists = []

def remove_noise(txt, delimiter = []):
    tks = word_tokenize(txt)
    cleaned = []
    for tk in tks:
        tk = re.sub('[^A-Za-z0-9]+','',tk)
        if len(tk) > 1 and tk.lower() not in delimiter:
            cleaned.append(tk.lower())
    return cleaned
  
for element in df['Description']:
    templists = remove_noise(element)
    for x in range(len(templists)):
        lists.append(templists[x])

dataframe = pd.DataFrame(lists)
dataframe.value_counts().loc[lambda x : x>3]
