def add_everything_up(a, b):
    try:
        result = a + b
        #print(result)
    except TypeError:
        print(str(a),str(b))
    else:
        print(result)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))