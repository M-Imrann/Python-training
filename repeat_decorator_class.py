class RepeatDecorator:
    def __init__(self, num):
        self.num = num

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(self.num):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper


@RepeatDecorator(3)
def greeting(name):
    return f"Hey {name}"


@RepeatDecorator(2)
def position(pos):
    return f"Hey {pos}"


print(greeting("Ali"))

print(position("I am Python Developer."))
