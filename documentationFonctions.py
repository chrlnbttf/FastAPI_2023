from fastapi import FastAPI
from fastapi import Header


# Personnalisation de l'API

api = FastAPI(
    title="My API",
    description="My own API powered by FastAPI.",
    version="1.0.1")


# Documentation du corps des fonctions
##  description ajoutée de la classe issue du modèle de BaseModel (visible dans schéma)
##  description ajoutée de la fonction (ajout commentaires à l'utilisation d'un endpoint)
##  header ajoutée à la fonction

from pydantic import BaseModel
from typing import Optional

class Computer(BaseModel):
    """a computer that is available in the store
    """
    computerid: int
    cpu: Optional[str]
    gpu: Optional[str]
    price: float

@api.put('/computer', name='Create a new computer')
def get_computer(computer: Computer):
    """Creates a new computer within the database
    """
    return computer


@api.get('/custom', name='Get custom header')
def get_content(custom_header: Optional[str] = Header(None, description='My own personal header')):
    return {
        'Custom-Header': custom_header
    }


