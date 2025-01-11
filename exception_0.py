def add_everything_up(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        if type(a) == int or isinstance(a, float) and type(b) == str:
                result = str(a) + b
        elif type(a) == str and isinstance(b, int) or isinstance(b, float):
                result = a + str(b)
    return result


print(add_everything_up(4,  'лисицы'))

print(add_everything_up('лисицы',  3.14))

print(add_everything_up(92, 3.14))
