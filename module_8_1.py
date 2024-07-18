def add_everything_up(a, b):
    result = a + b
    if isinstance(a, (int, float) and isinstance(b, (int, float))):
        return result
    if isinstance(a, str) and isinstance(b, str):
        return result
        #if isinstance(a, str) and isinstance(b, (int, float)):
            #return result
        #if isinstance(a, (int, float)) and isinstance(b, str):
            #return result
    else:
        raise TypeError
try:
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
except TypeError as exc:
    print(f'({exc})')
