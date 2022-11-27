""" Rutas para usuarios """
from fastapi import APIRouter

from config.db import conn

from schemas.user import (
    user_entity,
    users_entity
)
from models.user import User

user = APIRouter()

@user.get('/users')
def find_all_users():
    """ Retorna todos los usuarios """
    return users_entity(conn.eshop.user.find())

@user.post('/users')
async def create_user(user: User):
    """ Crea un usuario """
    new_user = dict(user)
    id = conn.eshop.user.insert_one(new_user).inserted_id
    return str(id)

@user.get('/users/{id}')
async def find_user():
    """ Obtiene un usuario """
    return "Usuario"

@user.put('/users/{id}')
async def update_user():
    """ Actualiza un usuario """
    return "Usuario"

@user.delete('/users/{id}')
async def delete_user():
    """ Elimina un usuario """
    return "Usuario"
