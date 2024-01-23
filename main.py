from fastapi import FastAPI

api = FastAPI()

@api.get('/')
def get_index(argument1):
    return {
        'data': argument1
    }