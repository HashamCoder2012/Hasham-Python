import pandas as pd
Exam_data={'name':['Jimmy','Chandler','Kaka','Joseph','Steve','Chris'],
           'scores':[125,9,16.5,np.nan,9,20,],
           'attempts':[4,3,2,2,3,1],
           'qualify':['yes','no','no','no','yes','yes']}
df=pd.DataFrame(Exam_data)
print("Summary of the basic information:")
print(df.info())