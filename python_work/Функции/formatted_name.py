def get_formatted_name(first_name, last_name, middle_name=''):
    """Возвращает отформатированное имя"""

    if middle_name:
        full_name = f"{first_name.title()} {middle_name} {last_name.title()}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name


musician = get_formatted_name('jimmi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)