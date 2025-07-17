from functools import wraps


def repeat(n, print_result=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper
    return decorator


@repeat(3, print_result=True)
def greeting(name):
    return f"Hey {name}"


@repeat(2, print_result=False)
def position(pos):
    return f"Hey {pos}"


print(greeting("Ali"))

print(position("I am Python Developer."))
