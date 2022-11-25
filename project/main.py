""" Archivo Principal de FastAPI """

from fastapi import FastAPI

from routes.user import user

app = FastAPI()

# De esta forma le aviso a FastAPI que agrego las rutas definidas.
app.include_router(user)
