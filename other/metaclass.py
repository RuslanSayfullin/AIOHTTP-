class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # Изменияем поведение класса, например, добавляем новый метод
        attrs['greeting'] = lambda self: print("Hello world!")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
obj.greeting()
