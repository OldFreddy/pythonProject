# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

print(" Дай мне два числа, и я поделю их")
print(' Введи q для выхода из программы')

while True:
    first_number = input("\nПервое число: ")
    if first_number == 'q':
        break
    second_number = input(("\nВторое число: "))
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Делить на ноль запрещено')
    else:
        print(answer)
