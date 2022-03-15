from datetime import timedelta, datetime
from typing import Optional
from models.models import Comic, User
from passlib.context import CryptContext
from bson import ObjectId
from jose import  jwt

from settings import ALGORITHM, SECRET_KEY

pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

def estructura_personaje(results):
    lista=[]
    for i in results:
        jsonData = {"id": i['id'], "name": i['name'],"image":i['thumbnail']['path'],"appearances":i['comics']['available']}
        lista.append(jsonData)
    return lista

def estructura_comic(results):
    lista=[]
    for i in results:
        jsonData={"id":i['id'],"title":i['title'],"image":i['thumbnail']['path'],"onsaledate":i["dates"][0]['date']}
        lista.append(jsonData)
    return lista


def get_password_hash(password):
    return pwd_context.hash(password)
    
def create_user(email, name,age, password):
    newuser=User()
    newuser.user_id = ObjectId()
    newuser.email = email
    newuser.name = name
    newuser.age=age
    newuser.password = get_password_hash(password)
    return dict(newuser)
    
def add_comic(comic):
    newcomic=Comic()
    newcomic.id=ObjectId()
    newcomic.id_comic=comic['id_comic']
    newcomic.title=comic['title']
    newcomic.image=comic['image']
    newcomic.onsaledate=comic['onsaledate']
    return dict(newcomic)
    
def create_access_token(data:dict,expires_delta:Optional[timedelta]=None):
    to_encode=data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    
