from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def car_type(self):
        pass


class Swift(Car):
    def car_type(self):
        return "This is hatchback"


class Fortuner(Car):
    def car_type(self):
        return "This is SUV"


s = Swift()
f = Fortuner()
print("Swift: ", s.car_type())
print("Fortuner: ", f.car_type())
