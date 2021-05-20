import os
from urllib.parse import urlparse
from .redis_client import RedisClient

redis_client = None

def get_redis_connection():
    global redis_client
    url = urlparse(os.environ.get('REDISCLOUD_URL'))
    if redis_client is None:
        return RedisClient(host=url.hostname, port=url.port, password=url.password)
    return redis_client