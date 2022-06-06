from usersClass import Admin, Privileges

my_new_admin = Admin("Lesha", "Maksimov", "Russia", "White", 34)
my_new_admin.describe_user()
my_new_admin.privileges.show_privileges()

# # user1 = User("SASHA", "VJHOPEDYRKA", "Russia", "WHITE", 26)
# # user1.describe_user()
# # user1.greet_user()
#
# new_user = User("SashaKakasha", "POPAJOPKA", "RUSSIA", "WHITE", 26)
# new_user.increment_attempts()
# print(new_user.login_attempts)
# new_user.reset_login_attemps()
# print(new_user.login_attempts)
#
# admin_user = Admin("Lesha", "Maksimov", "Russia", "White", "32")
# admin_user.describe_user()
# admin_user.privileges.show_privileges()
