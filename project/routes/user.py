""" Rutas para usuarios """
from fastapi import APIRouter

from config.db import conn

user = APIRouter()

@user.get('/users')
async def find_all_users():
    """ Retorna todos los usuarios """
    return "Usuario"

@user.post('/users')
async def create_user():
    """ Crea un usuario """
    return "Usuario"

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
