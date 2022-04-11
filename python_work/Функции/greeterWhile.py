def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное имя"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nTell me your name: ")
    print("\nPrint 'q' to quit ")

    f_name = input("Name is: ")
    if f_name == 'q':
        break
    l_name = input("Name is: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}")