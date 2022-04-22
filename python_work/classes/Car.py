class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Выводит пробег машины в милях"""
        print(f"thi car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометр"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("NELZYA MENSHE")

    def increment_odometer(self, miles):
        """Увеличивает показания обометра на заданное число"""
        self.odometer_reading += miles



my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.update_odometer(500)
my_new_car.update_odometer(300)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_new_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(200)
my_used_car.read_odometer()