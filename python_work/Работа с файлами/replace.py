file_path = 'txt_files/learning_python.txt'


with open(file_path) as file:
    for line in file:
        str_line = line
        str_line = str_line.replace('Python', 'C#')
        print(str_line)