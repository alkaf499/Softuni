def multiply(times):

    def decorator(function):
        def wrapper(params):
            result = times * function(params)
            return result

        return wrapper

    return decorator
