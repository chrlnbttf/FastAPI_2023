from fastapi import FastAPI

api = FastAPI(title = 'Exo')

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]


# Serveur paramètres (routage dynamique et chaîne de requêtes)

@api.get('/')
def get_index():
    return {
        "welcome" : "hello"
    }

@api.get('/users')
def get_users():
    return users_db

@api.get('/users/{userid:int}')
def get_user(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return user
    except IndexError:
        return {}

@api.get('/users/{userid:int}/name')
def get_user_name(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return {'name' : user['name']}
    except IndexError:
        return {}

@api.get('/users/{userid:int}/subscription')
def get_user_subscription(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return {'subscription' : user["subscription"]}
    except IndexError:
        return {}



# Serveur body

from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    userid: Optional[int]
    name: str
    subscription: str

@api.put('/users')
def put_users(user: User):
    new_id = max(users_db, key=lambda u: u.get('user_id'))['user_id']
    new_user = {
        'user_id': new_id + 1,
        'name': user.name,
        'subscription': user.subscription
    }
    users_db.append(new_user)
    return new_user

@api.post('/users/{userid:int}')
def post_users(user: User, userid):
    try:
        involved_user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        users_db.remove(involved_user)
        
        involved_user['name'] = user.name
        involved_user['subscription'] = user.subscription

        users_db.append(involved_user)
        return involved_user

    except IndexError:
        return {}

@api.delete('/users/{userid:int}')
def delete_users(userid):
    try:
        old_user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]

        users_db.remove(old_user)
        return {
            'userid': userid,
            'deleted': True
            }
       except IndexError:
        return {}


# Serveur header

from fastapi import Header

@api.get('/headers')
def get_headers(user_agent=Header(None)):
    return {
        'User-Agent': user_agent
    }