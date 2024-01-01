import datetime
from inspect import getcallargs


def logging_decorator(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            info = {
                'name': func.__name__,
                'arguments': getcallargs(func, *args, **kwargs),
                'call_time': datetime.datetime.now(),
                'result': func(*args, **kwargs)
            }
            logger.append(info)
            return info['result']
        return wrapper
    return decorator
