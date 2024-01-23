from fastapi import FastAPI

api = FastAPI(title = 'examen')

import pandas as pd

df_qcm = pd.read_csv('questions.csv',sep=',',header=0)

print(df_qcm)

@api.get('/qcm')
def get_qcm():
    return df_qcm




