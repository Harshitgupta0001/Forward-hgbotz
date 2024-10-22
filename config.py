import datetime
from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25492855")
    API_HASH = environ.get("API_HASH", "61876db014de51a4ace6b169608be4f1")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "Forward_HGBOT") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://david:surya@cluster12.f7tpy44.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Stubborn")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6359874284').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002346166150'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/hgbotz") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
