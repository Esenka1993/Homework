import io
def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i, string in enumerate(strings):
            strings_position = {}
            number_byte = file.tell()
            file.write(string + '\n')
            strings_position[(i, number_byte)] = string
        return strings_position



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)