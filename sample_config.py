import os

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
REDIS_URI = os.environ.get("REDIS_URI", None)
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
REDISPASSWORD = os.environ.get("REDISPASSWORD", None)
REDISHOST = os.environ.get("REDISHOST", None)
REDISUSER = os.environ.get("REDISUSER", None)
DATABASE_URL = os.environ.get("DATABASE_URL", None)
MONGO_URI = os.environ.get("MONGO_URI", None)
LOAD = []
NO_LOAD = []
MUST_JOIN = os.environ.get("MUST_JOIN", None)
auth_users = os.environ.get("AUTH_USERS", "5591734243")
AUTH_USERS = [int(num) for num in auth_users.split(",")]
