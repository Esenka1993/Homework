immutable_var='Key', 12, True
print(immutable_var)
immutable_var[1]=5
print(immutable_var) #нельзя изменить, потому что внутри кортежа нет элементов в квадратных скобках, которые можно было бы изменить
mutable_list=['vine', 'glass', True, 5]
mutable_list[2]=15
mutable_list[0]='cigarettes'
print(mutable_list)