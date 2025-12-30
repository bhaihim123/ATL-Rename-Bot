import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "30775734")
API_HASH = os.environ.get("API_HASH", "b7d8ccaedaac68008d12e3ee7f5ae867")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "8566325870:AAFQfTlvFz8C60kZLJCFdFKcvRIGJxMS5TY")

CHANNEL = os.environ.get("CHANNEL", "Ronituniverse") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","Ronits_file_renameer_bot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","BYNF_TamilChat") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","Ronituniverse") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","vnngffff")
STRING = os.environ.get("STRING", "AQHVmbYArKcX6tczjdHEkKWYJpKdgJ33JXRLHVH83E1DGjbUwlekuO7B7kQnEWxnscpPWXESnbEZt-G16lfMO9PtfkB5dFTY8JwfmmSKGZ7ZI83059-yTgsbHhIQ3BTr4yaWI86tCxVP9wj4aT0vTiPHmvXjGZuNw1QbcBcYLGnI_2rhQNMfBuP7UGWkzdnGyYERI6XrFqdiAyurkzgiVr7ccp2uhex65lKLyD2lz0OfXZWbu1CCuavGIK6-0g8rDchmnpgxHb2gE4SIihEnEjb-hX0WyIojvViODvShGJDjJQrT-dMT79PfyJftPATOwMTLUc4sl_B-C9NQ9Y6qnZEQSzLIIgAAAAHDihlMAA")

DB_NAME = os.environ.get("DB_NAME","renameone")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://bhaihim863:ds5P8DrfeVT5vkEi@cluster0.oacffum.mongodb.net/?appName=Cluster0")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7575574860').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003569385777"))
