from cache.redis import redis_client
from cache.serializers import (
    serialize,
    deserialize,
)


class CacheManager:

    @staticmethod
    def get(key):

        try:

            value = redis_client.get(key)

            if value is None:
                return None
            
            return deserialize(value)

        except Exception as e:
            # Log the error
            print(f"Error retrieving cache for key {key}: {e}")
            return None

    @staticmethod
    def set(
        key,
        value,
        ttl=3600,
    ):

        redis_client.set(
            key,
            serialize(value),
            ex=ttl,
        )

    @staticmethod
    def delete(key):

        redis_client.delete(key)

    @staticmethod
    def exists(key):

        return redis_client.exists(key)