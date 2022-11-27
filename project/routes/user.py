""" Rutas para usuarios """
from fastapi import APIRouter, Response

from config.db import conn

from schemas.user import (
    user_entity,
    users_entity
)
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


user = APIRouter()

@user.get('/users')
def find_all_users():
    """ Retorna todos los usuarios """
    return users_entity(conn.eshop.user.find())

@user.post('/users')
async def create_user(user: User):
    """ Crea un usuario """
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = conn.eshop.user.insert_one(new_user).inserted_id

    get_user = conn.eshop.user.find_one({"_id": id})

    return user_entity(get_user)

@user.get('/users/{id}')
async def find_user(id: str):
    """ Obtiene un usuario """
    return user_entity(conn.eshop.user.find_one({"_id": ObjectId(id)}))

@user.put('/users/{id}')
async def update_user(id: str, user: User):
    user2 = dict(user)

    """ Actualiza un usuario """
    if 'password' in user2:
        print('sssee')
        user2['password'] = sha256_crypt.encrypt(user2["password"])
    user_entity(conn.eshop.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": user2}))
    return user2

@user.delete('/users/{id}')
async def delete_user(id: str):
    """ Elimina un usuario """
    user_entity(conn.eshop.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
