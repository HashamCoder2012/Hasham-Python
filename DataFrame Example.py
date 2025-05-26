import pandas as pd
import numpy as np

exam_data={'name':['Anastasia','Dima','Katherine','Joseph','Steve','Chris'],
           'scores':[12.5,9,16.5,np.nan,9,20,],
           'attempts':[1,3,2,2,3,1],
           'qualify':['yes','no','yes','no','yes','no']}
labels=['a','b','c','d','e','z']
df=pd.DataFrame(exam_data,index=labels)
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())
print(df.head(3))
print(df.tail(2))
print(df.loc['b'])
