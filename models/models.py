from importlib.metadata import requires
from sqlite3 import Date
from typing import Optional
from unicodedata import name
from bson import ObjectId
from schematics.models import Model
from schematics.types import StringType, EmailType


class User(Model):
 
    user_id=ObjectId()
    email=EmailType(required=True)
    name=StringType(required=True)
    age=StringType(required=False)
    password=StringType(required=True)

class UserEmbed(Model):
    id=ObjectId()
    email=EmailType(required=True)
    name=StringType(required=True)

class Comic(Model):
    id=ObjectId()
    id_comic=StringType(required=True)
    title=StringType(required=True)
    image=StringType(required=True)
    onsaledate=StringType(required=True)
    user=UserEmbed()
    