class User():
    """Простой класс, описывающий пользователя"""

    def __init__(self, first_name, last_name, country, color, age, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.color = color
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"User name is {self.first_name} {self.last_name}\n"
              f"user country is {self.country}\n"
              f"user color is {self.color}\n"
              f"user age is {self.age}")

    def greet_user(self):
        print(f"GREETINGS {self.first_name} {self.last_name}")

    def increment_attempts(self):
        self.login_attempts += 1

    def reset_login_attemps(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, country, color, age):
        super().__init__(first_name, last_name, country, color, age)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                           "разрешено банить пользователей"]

    def show_privileges(self):
        print(self.privileges)


# user1 = User("SASHA", "VJHOPEDYRKA", "Russia", "WHITE", 26)
# user1.describe_user()
# user1.greet_user()

new_user = User("SashaKakasha", "POPAJOPKA", "RUSSIA", "WHITE", 26)
new_user.increment_attempts()
print(new_user.login_attempts)
new_user.reset_login_attemps()
print(new_user.login_attempts)

admin_user = Admin("Lesha", "Maksimov", "Russia", "White", "32")
admin_user.describe_user()
admin_user.privileges.show_privileges()
