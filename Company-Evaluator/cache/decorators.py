from functools import wraps


def cache(ttl=3600):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            return func(*args, **kwargs)

        return wrapper

    return decorator