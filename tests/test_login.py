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
#grant_type=&username=asd&password=u89&scope=&client_id=&client_secret=
#json={"email":"fake@gmail.com","password":"querty"}
@pytest.mark.asyncio
async def test_login():
    print("aqui")
    response= await login('json.loads({"username":"fake@gmail.com","password":"querty"})')
    print("doss")
    assert response.status_code==400
    #assert response.text=="Email o contraseña incorrecta"
