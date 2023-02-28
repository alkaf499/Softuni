def logged(func):
    def wrapper(*args):
        return f"you called {func.__name__}({', '.join(str(el) for el in args)})\nit returned {func(*args)}"

    return wrapper
