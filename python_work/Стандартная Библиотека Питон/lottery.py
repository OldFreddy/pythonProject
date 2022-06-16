from random import choice

nums_and_letters = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd')

win_combination = ''
new_combination = ''
count = 0
range_of_choice = 6

for i in range(range_of_choice):
    rnd_one = choice(nums_and_letters)
    win_combination = win_combination + str(rnd_one)

print(f"Выиграл билет с номером {win_combination}")


while new_combination != win_combination:
    count = count + 1
    print(new_combination)
    new_combination = ''

    for m in range(range_of_choice):
        rnd = choice(nums_and_letters)
        new_combination = new_combination + str(rnd)

print(f'столько шагов понадобилось для получения выигрышной комбинации - {count}')