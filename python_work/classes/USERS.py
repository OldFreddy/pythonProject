class User():
    """Простой класс, описывающий пользователя"""
    def __init__(self, first_name, last_name, country, color, age):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.color = color
        self.age = age

    def describe_user(self):
        print(f"User name is {self.first_name} {self.last_name}\n"
              f"user country is {self.country}\n"
              f"user color is {self.color}\n"
              f"user age is {self.age}")

    def greet_user(self):
        print(f"GREETINGS {self.first_name} {self.last_name}")


user1 = User("SASHA", "VJHOPEDYRKA", "Russia", "WHITE", 26)
user1.describe_user()
user1.greet_user()