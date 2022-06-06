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
