import time


class TimingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"Function {self.func.__name__} execution time is : "
              f"{end - start: .5f} seconds")
        return result


@TimingDecorator
def slow():
    time.sleep(5)
    return "Slow Function Executed."


@TimingDecorator
def medium():
    time.sleep(2)
    return "Medium Function Executed."


@TimingDecorator
def fast(num):
    for i in range(num):
        return "Fast Function Executed."


print(slow())

print(medium())

print(fast(5))
