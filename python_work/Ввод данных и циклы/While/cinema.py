flag = True
prompt = "Enter you age "
while flag:
    age = input(prompt)
    if int(age) < 3:
        print('Free Entrance')
        break
    elif 3 < int(age) < 12:
        print('10$')
        break
    else:
        print("15$")
        break


