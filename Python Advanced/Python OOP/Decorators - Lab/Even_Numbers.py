from functools import wraps


def even_numbers(function):

    @wraps(function)
    def wrapper(*args):
        result = function(*args)

        return [num for num in result if num % 2 ==0]

    return wrapper
