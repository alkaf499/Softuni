def genrange(start: int, end: int):
    num = start

    while num <= end:
        yield num
        num += 1
