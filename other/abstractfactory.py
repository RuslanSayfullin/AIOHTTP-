from abc import ABC, abstractmethod

# Abstract Product
class AbstractProduct(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Products
class ConcreteProductA(AbstractProduct):
    def operation(self):
        return "ConcreteProductA operation"

class ConcreteProductB(AbstractProduct):
    def operation(self):
        return "ConcreteProductB operation"

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self):
        pass

# Concrete Factories
class ConcreteFactory1(AbstractProduct):
    def create_product(self):
        return ConcreteProductA()

# Concrete Factories
class ConcreteFactory2(AbstractProduct):
    def create_product(self):
        return ConcreteProductB()

# Usage
factory1 =  ConcreteFactory1()
product1 = factory1.create_product()
print(product1.operation()) # Output: "ConcreteProductA operation"

factory2 = ConcreteFactory2()
product2 = factory2.create_product()
print(product2.operation()) # Output: "ConcreteProductB operation"




