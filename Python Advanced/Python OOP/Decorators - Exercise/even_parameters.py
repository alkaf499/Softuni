def even_parameters(func):
    def wrapper(*args):
        all_even = False
        for el in args:
            if isinstance(el, int):
                if el % 2 == 0:
                    continue

            return 'Please use only even numbers!'

        return func(*args)

    return wrapper
