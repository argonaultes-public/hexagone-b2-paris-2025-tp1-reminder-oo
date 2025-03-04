from abc import ABC, abstractmethod


class Fly(ABC):

    @abstractmethod
    def fly(self):
        pass

class FlyWell(Fly):

    def fly(self):
        print(f'... is flying well!')

class FlyNone(Fly):

    def fly(self):
        print('Cannot fly')

class Quack(ABC):

    @abstractmethod
    def quack(self):
        pass

class QuackQuack(Quack):

    def quack(self):
        print('quack quack!')

class QuackCoin(Quack):

    def quack(self):
        print('coin coin!')

class QuackSquick(Quack):

    def quack(self):
        print('squick squick!')

class Duck(ABC):
    def __init__(self, name, fly: Fly, quack: Quack):
        self.__name = name
        self.__fly = fly
        self.__quack = quack

    @property
    def name(self):
        return self.__name

    def set_fly(self, fly: Fly):
        self.__fly = fly

    def fly(self):
        self.__fly.fly()

    def quack(self):
        self.__quack.quack()

class NormandyDuck(Duck):
    def __init__(self, name):
        super().__init__(name, FlyWell(), QuackQuack())


class MallardDuck(Duck):
    def __init__(self, name):
        super().__init__(name, FlyWell(), QuackCoin())


class RubberDuck(Duck):
    def __init__(self, name):
        super().__init__(name, FlyNone(), QuackSquick())



if __name__ == '__main__':
    duck1 = NormandyDuck('donald')
    duck1.fly()
    duck1.quack()
    picsou = MallardDuck('picsou')
    picsou.fly()
    picsou.quack()
    yellow = RubberDuck('yellow')
    yellow.fly()
    yellow.set_fly(FlyWell())
    yellow.fly() # flying well....