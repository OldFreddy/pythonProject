favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
language = favorite_languages['sarah'].title()
language = favorite_languages['edward'].title()
print(language)

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(name.title())




print("\n______________________________")

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language}")

print("\n______________________________")

for key in favorite_languages.keys():
    print(key.title())

print("\n______________________________")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f'\tПривет, {name}, вижу, ты любишь {language}')


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, get out")



print('\n_________________________________')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name}, thank you")

print('\n_________________________________')

#Перебор значений в словаре

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

print("The following languages have ben mentioned:")
for language in favorite_languages.values():
    print(language.title())

print('\n_________________________________')

for language in sorted(favorite_languages.values()):
    print(language.title())
print('\n_________________________________')
for language in set(favorite_languages.values()):
    print(language.title())

print('\n_________________________________')
for language in sorted(set(favorite_languages.values())):
    print(language.title())

print('\n_________________________________')

people = ['phil', 'sarah', 'vova', 'nikitos']

for human in people:
    if human in favorite_languages.keys():
        print(f'Hello {human.title()}, ty for oprose')
    else:
        print(f'Hello {human}, lets oprose')