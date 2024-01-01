from time import time


def time_decorator(func):
    def wrapper():
        start = time()
        result = func()
        end = time()
        print(round(end-start))
        return result
    return wrapper
