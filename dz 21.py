# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые
# для работы методы.




from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Blender(Device):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def start(self):
        print(f"{self.brand} {self.model} - включен, скорость: {self.speed}")

    def stop(self):
        print(f"{self.brand} {self.model} - выключен")


class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def start(self):
        print(f"{self.brand} {self.model} - включен, мощность: {self.power} Вт")

    def stop(self):
        print(f"{self.brand} {self.model} - выключен")


blender = Blender("Braun", "BX1000", 5)
blender.start()
blender.stop()
meat_grinder = MeatGrinder("Kenwood", "MG450", 1200)
meat_grinder.start()
meat_grinder.stop()










# 2 задание

# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.


class Ship:
    def __init__(self, name, length, crew):
        self.name = name
        self.length = length
        self.crew = crew

    def sail(self):
        print(f"{self.name} плывет по волнам.")

class Frigate(Ship):
    def sail(self):
        print(f"Фрегат {self.name} идет в море.")

class Destroyer(Ship):
    def sail(self):
        print(f"Эсминец {self.name} отправляется в плаванье.")

class Cruiser(Ship):
    def sail(self):
        print(f"Крейсер {self.name} выходит в открытое море.")

# Пример использования классов
frigate = Frigate("Фрегат Alpha", 150, 200)
destroyer = Destroyer("Эсминец Bravo", 200, 300)
cruiser = Cruiser("Крейсер Charlie", 250, 400)

frigate.sail()
destroyer.sail()
cruiser.sail()

