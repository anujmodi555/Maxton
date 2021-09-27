def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lower = func.lower()
        return string_lower
    return wrapper


@lowercase_decorator
def hello():
    return "Hello World"

print(hello())