class Restaurant():
    """Просто класс ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Kitchen is {self.cuisine_type}")

    def open_restaurant(self):
        print("OPEN OPEN OPEN")

restaurant = Restaurant("PIVOLET", "PITPIVO")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

new_restaurant = Restaurant("RIS", "ROLLY")
new_restaurant.describe_restaurant()