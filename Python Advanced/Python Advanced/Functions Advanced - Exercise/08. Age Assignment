def age_assignment(*args, **kwargs):
    result = ""
    for name in args:
        for key in kwargs:
            if name[0] == key:
                # kwargs[name] = kwargs.pop(key)
                kwargs[name] = kwargs[key]
                del kwargs[key]
                break
    for name, age in sorted(kwargs.items(), key= lambda x: x[0]):
        result += f"{name} is {age} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
