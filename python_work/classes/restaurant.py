class Restaurant():
    """Просто класс ресторана"""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Kitchen is {self.cuisine_type}")

    def open_restaurant(self):
        print("OPEN OPEN OPEN")

    def set_number_served(self, number_serverd_people):
        self.number_served = number_serverd_people

    def increment_number_served(self, number_to_increment):
        self.number_served += number_to_increment


restaurant = Restaurant("PIVOLET", "PITPIVO")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

new_restaurant = Restaurant("RIS", "ROLLY")
new_restaurant.describe_restaurant()

very_new_restaurant = Restaurant('Some Restik', "kavkaz", 10)
print(f'{very_new_restaurant.number_served} people')
very_new_restaurant.set_number_served(25)
print(f'{very_new_restaurant.number_served} people')

very_new_restaurant.increment_number_served(25)
print(f'{very_new_restaurant.number_served} people')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["sort1", "sort2", "sort3", "sort4"]

    def get_sots_of_iceCream(self):
        print(self.flavors)


iceCream_restaurant = IceCreamStand("IceCreamForAss", "IceCream")
iceCream_restaurant.describe_restaurant()
iceCream_restaurant.get_sots_of_iceCream()
