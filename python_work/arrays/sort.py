cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("SORTIROVKA")
cars.sort()
print(cars)
print('SORTIROVKA_OBRATNAYA')
cars.sort(reverse=True)
print(cars)

print("\n Временная сортировка")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True))
print(cars)

print("\nВывод списка в обратном порядке")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

print('\nОпределение длины списка')
a = len(cars)
print("Длина списка = " + str(a))
print(f"Длина списка равна {a}")
