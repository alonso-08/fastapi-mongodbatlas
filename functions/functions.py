from models.models import Comic, User
from passlib.context import CryptContext
from bson import ObjectId


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
    
def create_user(email, username,age, password):
    newuser=User()
    newuser.user_id = ObjectId()
    newuser.email = email
    newuser.name = username
    newuser.age=age
    newuser.password = get_password_hash(password)
    return dict(newuser)
    
def addComic(comic):
    newcomic=Comic()
    newcomic.id=ObjectId()
    newcomic.id_comic=comic['id_comic']
    newcomic.title=comic['title']
    newcomic.image=comic['image']
    newcomic.onsaledate=comic['onsaledate']
    return dict(newcomic)

pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')