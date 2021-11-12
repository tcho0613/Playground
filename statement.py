import pandas as pd
import numpy as np

df = pd.read_csv('statement.CSV')
df = df.drop(['Memo'],axis=1)
df.head()
