from ast import Str
from datetime import timedelta, datetime
from operator import imod
import sys
import os
from urllib import response

from functions.functions import addComic, create_access_token, create_user, estructura_comic, estructura_personaje, pwd_context
from settings import ALGORITHM, JWT_SECRET_KEY, SECRET_KEY
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import os
from unittest import result
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr, Json
from jose import JWTError, jwt
from typing import Optional, List

from marvel import Marvel
import json
from models.models import Comic, ItemComic, User, UserEmbed
import connection
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, OAuth2AuthorizationCodeBearer
from fastapi import Depends, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext



app = FastAPI()



m=Marvel('35475389d5c62cff1e1585c3a30847b2','1fdbc9f56cc947679bacc8e70c2219c1e4698887')




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")



@app.get("/searchComics/")
def get_comics_or_characters(option: Optional[str]=None,word: Optional[str]=None):
    if option=='personaje' and  word:#searchComic/personaje/palabra
        results=m.characters.all(limit=100)        
        results=results['data']['results']     
        results=estructura_personaje(results)   
        lista=[]
        lista_personajes=[]
        for item in results:
            if word.lower() in item['name'].lower():
                lista_personajes.append(item)        
        lista.append(lista_personajes)
        lista.append([])    
        results=lista
        return results

    elif option=='personaje' and not word:
        results=m.characters.all()
        results=results['data']['results']
        results=estructura_personaje(results) 
        lista=[]
        lista.append(result)
        lista.append([])
        return results
        
    elif option=='comic' and word :#searchComic/comic/palabra        
        results=m.comics.all()
        results=results['data']['results']
        results=estructura_comic(results) 
        lista=[]
        lista_comics=[]
        for item in results:            
            if  isinstance(word, str):                
                if word.lower() in item['title'].lower():
                    lista_comics.append(item)
            else:
                if word ==item['id']:                    
                    lista_comics.append(item)

            
        lista.append([])
        lista.append(lista_comics)
        results=lista
        return results

    elif option=='comic' and not word:
        results=m.comics.all()
        results=results['data']['results']    
        results=estructura_comic(results) 
        lista=[]
        lista.append([])
        lista.append(lista)
        
        results=lista
        return results
    elif option=='all' and word:#searchComic/all/palabra/(personajes y comics)
        personajes=m.characters.all()
        personajes=personajes['data']['results']
        personajes=estructura_personaje(personajes)
        lista=[]
        lista_personajes=[]
        for item in personajes:
            if word.lower() in item['name'].lower():
                lista_personajes.append(item)  

        comics=m.comics.all()
        comics=comics['data']['results']
        comics=estructura_comic(comics)
        lista_comics=[]
        for item in comics:
            if word.lower() in item['title'].lower():
                lista_comics.append(item)
        lista.append(lista_personajes)
        lista.append(lista_comics)
        results=lista
        
    elif option=='all' and not word:
        personajes=m.characters.all()
        personajes=personajes['data']['results']
        personajes=estructura_personaje(personajes)

        comics=m.comics.all()
        comics=comics['data']['results']
        comics=estructura_comic(comics)
        lista=[]
        lista.append(personajes)
        lista.append(comics)
        results=lista
    else:
        return [[],[]]
    return results








#Ruta para pruebas
@app.post("/comics")
def comics():

    results=m.characters.comics(1011334)
    return results



@app.post("/addToLayaway")
async def addmyComic(comic:ItemComic,token:str=Depends(oauth2_scheme)):
    #Decodificamos el token para poder acceder a su contenido
    token_bonito=jwt.decode(token,SECRET_KEY,ALGORITHM) 
    #Buscamos el comic que nos mandan en la API de Maverl, usando la funcion creada anteriormente
    comic_search=get_comics_or_characters('comic',comic.id_comic) 
    #Accedemos al segundo array de comic_search y validamos si hay resultados
    if len(comic_search[1])>0:#Si hay resultados obtenemos los datos del comic        
        id_comic=comic_search[1][0]['id']    
        title_comic=comic_search[1][0]['title']
        image_comic=comic_search[1][0]['image']
        onsaledate_comic=comic_search[1][0]['onsaledate']   
        #Creamos un objeto json con los datos del comic
        object_comic={"id_comic":id_comic,"title":title_comic,"image":image_comic,"onsaledate":onsaledate_comic} 
        #Buscamos el comic en nuestra DB
        #comic_exist=connection.db.comics.find({"id_comic":id_comic})
        
        #if comic_exist:
        comic=addComic(object_comic)    
        comic['user']={"email":token_bonito['email'],"name":token_bonito['name']}    
        connection.db.comics_user.insert_one(comic)    
        response={'message':'Comic registrado correctamente',"comic":json.loads(json.dumps(comic,default=str))}
        #else:
        #response={'message':'El comic no existe '}
    else:
        response={'message':'El comic no existe en la DB de Marvel '}
    return response



@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_exist= await connection.db.users.find_one({'email':form_data.username})    
    if not user_exist:
        raise HTTPException(status_code=400, detail="Email o contraseña incorrecta")
    

    password_check=pwd_context.verify(form_data.password,user_exist['password'])
    if password_check:
        access_token=create_access_token(data={"email":user_exist["email"],"name":user_exist["name"]},expires_delta=timedelta(minutes=30))
        return {"email":user_exist["email"],"name":user_exist["name"],"age":user_exist["age"],"access_token":access_token}

    else:
        raise HTTPException(status_code=400,detail="contraseña incorrecta")
  

@app.get("/getLayawayList")
async def GetMyComics(token:str=Depends(oauth2_scheme)):
    token_bonito=jwt.decode(token,SECRET_KEY,ALGORITHM)
    email=token_bonito["email"]
    #Para acceder a un doc incrustado se usa asi { "user.name": 'tichu'  }
    all_comics=await connection.db.comics_user.find({"user.email":email}).to_list(1000)   
        
    response={"mis_comics":json.loads(json.dumps(all_comics,default=str))}
    return response

# Signup endpoint with the POST method
@app.post("/users/register/")
async def signup(email, name: str,age:int, password: str):
    data = create_user(email, name,age, password)
    if isinstance(data['age'],int):
        # Covert data to dict so it can be easily inserted to MongoDB
        dict(data)

        # Checks if an email exists from the collection of users
        user_exist= await connection.db.users.find_one({'email': data['email']})
        if user_exist: 
            return {"message":"El email ya existe en la base de datos"}
        # If the email doesn't exist, create the user
        else:
            await connection.db.users.insert_one(data)
            return {"message":"User Created","email": data['email'], "name": data['name'], "pass": data['password']}

    else:
        return {"message":"El campo edad debe ser un número"}


