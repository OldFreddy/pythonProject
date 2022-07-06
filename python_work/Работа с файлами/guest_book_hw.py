filename = 'txt_files/guest_book.txt'
a = 0

with open(filename, 'a') as file_object:
    while a < 3:
        guest_name = input('Представьтесь\n')
        file_object.write(guest_name + ' \n')
        a+=1