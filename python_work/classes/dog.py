class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализирует аргументы name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name} rolled over")


my_dog = Dog("Willie", 6)
you_dog = Dog("Lucy", 7)

print(f"My dog's name is {my_dog.name}.")
print(f"Your dog's name is {you_dog.name}.")
print(f"My dog is {my_dog.age} years old")
print(f"Your dog is {you_dog.age} years old")
my_dog.sit()
my_dog.roll_over()
you_dog.sit()
you_dog.roll_over()
