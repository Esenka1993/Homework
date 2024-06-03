def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(1, 'строка')
print_params(1,True)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ['длина', 15, True]
values_dict = {'a': 10, 'b': 'ширина', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [36.6, 'temperature']
print_params(*values_list_2, 42)