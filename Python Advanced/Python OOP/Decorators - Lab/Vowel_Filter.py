from functools import wraps


def vowel_filter(function):
    vowels = "aeiouAEIOU"

    @wraps(function)
    def wrapper():
        result = function()
        return [l for l in result if l.lower() in vowels]

    return wrapper
