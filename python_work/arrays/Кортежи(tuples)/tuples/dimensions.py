dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250  не сработает, потому что это неизменяемый список(кортеж)

for dimension in dimensions:
    print(dimension)

print('Original dimensions ')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 200)
print('\n Modified dimensoins ')
for dimension in dimensions:
    print(dimension)