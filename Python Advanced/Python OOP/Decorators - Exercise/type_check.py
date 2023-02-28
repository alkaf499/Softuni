def type_check(expexted_type):
    def decorator(func):
        def wrapper(arg):
            if isinstance(arg, expexted_type):
                return func(arg)

            return 'Bad Type'
        return wrapper
    return decorator
