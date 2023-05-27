from enum import Enum, auto

class Car(Enum):
    VOLGA = auto()
    FERRARI = auto()
    RENAULT = auto()
print(Car.VOLGA)    # Car.VOLGA

for car in Car:
    print(car, end=" ")
