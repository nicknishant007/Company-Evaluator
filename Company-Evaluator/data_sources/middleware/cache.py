from functools import wraps

from cache.manager import CacheManager
from observability import app_logger


def cache_response(
    ttl: int = 3600,
):
    def decorator(func):

        @wraps(func)
        async def wrapper(
            self,
            ticker: str,
            *args,
            **kwargs,
        ):

            cache_key = (
                f"{self.__class__.__name__}:"
                f"{func.__name__}:"
                f"{ticker}"
            )

            cached_data = (
                CacheManager.get(
                    cache_key
                )
            )

            if cached_data:
                app_logger.info(
                    "Cache hit for %s",
                    cache_key,
                )

                return cached_data

            result = await func(
                self,
                ticker,
                *args,
                **kwargs,
            )

            CacheManager.set(
                cache_key,
                result,
                ttl,
            )

            return result

        return wrapper

    return decorator