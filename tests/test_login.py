'''
#grant_type=&username=asd&password=u89&scope=&client_id=&client_secret=
#json={"email":"fake@gmail.com","password":"querty"}
@pytest.mark.asyncio
async def test_login():
    print("aqui")
    response= await login('json.loads({"username":"fake@gmail.com","password":"querty"})')
    print("doss")
    assert response.status_code==400
    #assert response.text=="Email o contraseña incorrecta"

from http import client
import json
from operator import imod
import os
import sys
from urllib import response
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from fastapi.testclient import TestClient
from app import app, login
import pytest

client=TestClient(app)


'''
from http import client
import json
import os
import sys
import warnings

import pytest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from app import app
from urllib import response
from fastapi.testclient import TestClient
client=TestClient(app)


def test_get_comics_or_characters():
    option="personaje"
    word="man"
    response = client.get(f'/searchComics/{option}/{word}')
    print(response.request)
    assert response.status_code == 200    
    #assert response.json() == [[],[]]

def test_singup():
    email='luis9@gmail.com'
    name='tichu'
    age=23
    password='tichu'
    response=client.post(f'/users/register/{email}/{name}/{age}/{password}')
    assert response.status_code==200
    assert response.json()=={'message':'El email ya existe en la base de datos'}
