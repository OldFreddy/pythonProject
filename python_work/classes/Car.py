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

    def fill_gas_tank(self):
        """Заправляем автомобиль бензином"""
        print("Автомобиль заправлен")


class Battery():
    """Простая модель аккумулятора электромобиля"""

    def __init__(self, battery_size=75):
        """Инициализирует атрибуты класса"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Выводит приблизительный запас хода аккумулятора"""
        if self.battery_size == 75:
            range_of_battery= 260
        elif self.battery_size == 100:
            range_of_battery = 315

        print(f"This car can go about {range_of_battery} miles on a full charge")

class Electro_Car(Car):
    """Представляют аспекты машины, специфические для электромобилей"""

    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Выводит информацию о мощности аккумуляторов"""
        print(f"This car has a {self.battery} kWh battery")

    def fill_gas_tank(self):
        """У электромобиля нет бензобака"""
        print("Сюда не нужно заливать бензин, это электромобиль, ты что, дурачок?")


my_tesla = Electro_Car('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
