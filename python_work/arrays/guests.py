guests = ["stalin" , "beria", "chaplin"]

print(f"Привет, {guests[0]}")
print(f"Привет, {guests[1]}")
print(f"Привет, {guests[-1]}")

print(guests[1] + " Удалить")

guests[1] = "NEBERIA"
print(guests)
print(f"Привет, {guests[0]}")
print(f"Привет, {guests[1]}")
print(f"Привет, {guests[-1]}")

print(guests)
print("теперь список гостей расширяется")

guests.insert(0, "Добавленный гость в начало")
guests.insert(2, "Добавленный гость в вередину")
guests.append("Добавленный гость в конец")
print(guests)
print(f"Привет, {guests[0]}")
print(f"Привет, {guests[1]}")
print(f"Привет, {guests[2]}")
print(f"Привет, {guests[3]}")
print(f"Привет, {guests[4]}")
print(f"Привет, {guests[5]}")

#сокращение списка гостей

print("только двоих оставляем")
guests.pop(-1)
guests.pop(-1)
guests.pop(-1)
guests.pop(1)
print(guests)

#del guests[0]
#del guests[0]
print(guests)

print("Количество гостей равно " + str(len(guests)))