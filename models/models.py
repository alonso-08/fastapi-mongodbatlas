from importlib.metadata import requires
from sqlite3 import Date
from typing import Optional
from unicodedata import name
from bson import ObjectId
from pydantic import BaseModel
from schematics.models import Model
from schematics.types import StringType, EmailType

#Clase para crear el usuario
class User(Model):
 
    user_id=ObjectId()
    email=EmailType(required=True)
    name=StringType(required=True)
    age=StringType(required=False)
    password=StringType(required=True)

#Clase base que se utilizará para agregarlo a un comic
class UserEmbed(Model):
    id=ObjectId()
    email=EmailType(required=True)
    name=StringType(required=True)

#Clase para modelar el comic a crear
class Comic(Model):
    id=ObjectId()
    id_comic=StringType(required=True)
    title=StringType(required=True)
    image=StringType(required=True)
    onsaledate=StringType(required=True)
    user=UserEmbed()

#Clase base para asignarle el tipo al comic 
class ItemComic(BaseModel):
    id_comic:int
  