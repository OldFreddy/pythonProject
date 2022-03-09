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
