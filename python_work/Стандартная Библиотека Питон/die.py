import random


class Die():
    """Простая модель кубика"""

    def __init__(self, sides=6):
        """Инициализирует атрибут описания кубика"""
        self.sides = sides

    def roll_random(self):
        """Бросок кубика"""
        print(f"Количество сторон равно {self.sides}")
        return random.randint(1, self.sides)
