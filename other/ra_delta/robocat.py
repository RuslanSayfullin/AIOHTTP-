class Animal:
    def say(self):
        print('i am animal')


class Cat(Animal):
    pass


class Robot:
    def say(self):
        print('i am robot')


class RoboCat(Cat, Robot):
    pass


robo = RoboCat()
robo.say()