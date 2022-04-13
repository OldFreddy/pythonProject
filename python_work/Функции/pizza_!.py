def make_pizza(size, *toppings):
    """Opisanie picci"""

    print(f"\nMaking a {size} -inch pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")


make_pizza(30, "pepperronnnni")

make_pizza(100, "dlkjs" , "ldkdlkj", "kjsdlks")