import time
from functools import wraps


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} executed in "
              f"{end - start: .5f} seconds.")
        return result
    return wrapper


@timing_decorator
def slow():
    time.sleep(5)
    return "Slow Function Executed."


@timing_decorator
def medium():
    time.sleep(2)
    return "Medium Function Executed."


@timing_decorator
def fast(num):
    for i in range(num):
        return "Fast Function Executed."


print(slow())

print(medium())

print(fast(5))
