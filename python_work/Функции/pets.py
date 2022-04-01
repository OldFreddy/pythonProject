def describe_pet(animal_type='dog', pet_name=''):
    """Выводит информацию о животном"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


describe_pet("Dog", "SOLOMA")
describe_pet("Cat", "KOSHKA")
describe_pet(animal_type="hamster", pet_name="SSS")
describe_pet(pet_name='Willy')


