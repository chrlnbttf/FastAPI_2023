from fastapi import FastAPI
from fastapi import Header


api = FastAPI(openapi_tags=[
    {
        'name': 'home',
        'description': 'default functions'
    },
    {
        'name': 'items',
        'description': 'functions that are used to deal with items'
    }
])

# Documentation du corps des fonctions
##  description ajoutée de la classe issue du modèle de BaseModel (visible dans schéma)
##  description ajoutée de la fonction (ajout commentaires à l'utilisation d'un endpoint)
##  header ajoutée à la fonction

