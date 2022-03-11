from operator import imod
from pymongo import MongoClient
import settings
import motor.motor_asyncio


#client=MongoClient(settings.mongdb_uri,settings.port)
#db=client['coppel_db']
client = motor.motor_asyncio.AsyncIOMotorClient(settings.DB_URL)
db = client['coppel_db']