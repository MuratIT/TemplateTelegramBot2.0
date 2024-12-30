from decouple import config

TOKEN = config('TOKEN')
BASE_URL = config('BASE_URL')
WEBHOOK_PATH = config('WEBHOOK_PATH')

REDIS_URL = config('REDIS_URL')