file_path = 'txt_files/learning_python.txt'
list_of_file_lines = []

with open(file_path) as file:
    content = file.read()
print(content)

print('____________________\n')

with open(file_path) as file:
    for line in file:
        print(line.strip())

with open(file_path) as file:
    list_of_file_lines = file.readlines()

print('____________________\n')

print(list_of_file_lines)
for line in list_of_file_lines:
    print(line.strip())