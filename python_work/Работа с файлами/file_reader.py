# file_path = 'c:/pi_digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents)

'''Чтение по строкам'''
file_path = 'c:/pi_digits.txt'
# with open(file_path) as file:
#     for line in file:
#         print(line.rstrip())


'''Создание списка строк по содержимому файла'''
# with open(file_path) as file:
#     lines = file.readlines()
#
# for line in lines:
#     print(line.rstrip())

'''Работа с содержимым файла'''
# with open(file_path) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))

# ПРИМЕЧАНИЕ Читая данные из текстового файла, Python интерпретирует весь текст
# в файле как строку Если вы читаете из текстового файла число и хотите работать с ним
# в числовом контексте, преобразуйте его в целое число функцией int() или в вещественное число функцией float()



'''Большие файлы: миллион цифр'''

file_path = ''
print(f'{file_path} tut pustoy put')
file_path = 'c:/pi_million_digits.txt'
print(file_path)
with open(file_path) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

print(f'{pi_string[:6121252]}...')
print(len(pi_string))