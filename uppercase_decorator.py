def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase_decorator
def greeting():
    return "Hey, I am Muhammad Imran."


print(greeting())
