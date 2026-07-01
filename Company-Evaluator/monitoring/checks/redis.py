from cache.redis import redis_client


async def check_redis():

    try:

        redis_client.ping()

        return True

    except Exception:

        return False