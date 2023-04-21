def logging(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        func(*args, **kwargs)

    return wrapper


@logging
def add(x, y):
    print(x + y)
    return x + y


add(1, 2)