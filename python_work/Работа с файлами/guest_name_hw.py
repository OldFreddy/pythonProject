filename = 'txt_files/guest_name.txt'

with open(filename, 'w') as file_object:
    guest_name = input('Представьтесь \n')
    file_object.write(guest_name)