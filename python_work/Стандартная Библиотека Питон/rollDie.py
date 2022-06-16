from die import Die

newDie = Die()

for i in range(10):
    print(newDie.roll_random())

die_10_sides = Die(10)
for i in range(10):
    print(die_10_sides.roll_random())

die_20_sides = Die(20)
for i in range(10):
    print(die_20_sides.roll_random())
