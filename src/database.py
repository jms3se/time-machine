from redis import Redis

import config

def get_redis_connection():
    redis_connection = Redis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=config.REDIS_DB,
        decode_responses=config.REDIS_DECODE_RESPONSES
    )

    return redis_connection
