from restaurant import Restaurant

my_new_restaurant = Restaurant('RESTFORALL', 'PIVOandVodka', 10)
my_new_restaurant.describe_restaurant()

# restaurant = Restaurant("PIVOLET", "PITPIVO")
#
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# new_restaurant = Restaurant("RIS", "ROLLY")
# new_restaurant.describe_restaurant()
#
# very_new_restaurant = Restaurant('Some Restik', "kavkaz", 10)
# print(f'{very_new_restaurant.number_served} people')
# very_new_restaurant.set_number_served(25)
# print(f'{very_new_restaurant.number_served} people')
#
# very_new_restaurant.increment_number_served(25)
# print(f'{very_new_restaurant.number_served} people')
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ["sort1", "sort2", "sort3", "sort4"]
#
#     def get_sots_of_iceCream(self):
#         print(self.flavors)
#
#
# iceCream_restaurant = IceCreamStand("IceCreamForAss", "IceCream")
# iceCream_restaurant.describe_restaurant()
# iceCream_restaurant.get_sots_of_iceCream()
