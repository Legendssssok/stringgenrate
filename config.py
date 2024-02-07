import os

API_ID = 11573285
API_HASH = "f2cc3fdc32197c8fbaae9d0bf69d2033"
BOT_TOKEN = "6122169010:AAEavMTJpHfLfsEEuuLXK-sjWzzjP9Y6uJA"
REDIS_URI = None
REDIS_PASSWORD = None
REDISPASSWORD = os.environ.get("REDISPASSWORD", None)
REDISHOST = os.environ.get("REDISHOST", None)
REDISUSER = os.environ.get("REDISUSER", None)
DATABASE_URL = os.environ.get("DATABASE_URL", None)
MONGO_URI = os.environ.get("MONGO_URI", None)
