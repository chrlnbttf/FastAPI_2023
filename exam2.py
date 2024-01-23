from fastapi import FastAPI

import csv

api = FastAPI(title = 'examen')

with open('questions.csv', newline='') as f:
    reader = csv.reader(f)
    qcm_db = list(reader)

print(qcm_db)

@api.get('/qcm')
def get_qcm():
    return qcm_db

@api.get('/users/{userid:int}')
def get_user(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return user
    except IndexError:
        return {}
