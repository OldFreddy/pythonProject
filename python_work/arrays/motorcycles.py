motorcucles = ['honda', 'yamaha', 'suzuki']
print(motorcucles)

motorcucles[0] = 'ducati'
print(motorcucles)

motorcucles.append('ducati')  # добавление элемента в конец списка
print(motorcucles)

motorcucles = []
motorcucles.append('hondaa')
motorcucles.append('yamahaa')
motorcucles.append('suzukii')
print(motorcucles)

motorcucles.insert(0, "privet")  # вставка элемента на определенное место
print(motorcucles)

del motorcucles[0]
print(motorcucles)

motorcucles = ['honda', 'yamaha', 'suzuki']
print(motorcucles)

popped_motorcucles = motorcucles.pop()
print(motorcucles)
print(popped_motorcucles)

motorcucles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcucles.pop()  # посделний элемент
print(f"The last motorcucle I owned was a {last_owned.title()}.")

first_owned = motorcucles.pop(0)
print(f"The first motorcucle I owned was a {first_owned.upper()}")

motorcucles = ['honda', 'yamaha', 'suzuki']
print(motorcucles)
motorcucles.remove('yamaha')
print(motorcucles)