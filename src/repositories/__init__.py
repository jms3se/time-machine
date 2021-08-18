from redis import Redis

from src import config

def get_redis_connection():
    jwt_redis_blocklist = Redis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=config.REDIS_DB,
        decode_responses=config.REDIS_DECODE_RESPONSES
    )

    return jwt_redis_blocklist

from .user import UserRepository
from .blocklist import BlocklistRepository
