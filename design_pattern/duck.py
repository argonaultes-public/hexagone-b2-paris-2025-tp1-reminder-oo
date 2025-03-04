from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def quack(self):
        pass

class NormandyDuck(Duck):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f'{self.name} ({self.__class__}) is flying well!')


    def quack(self):
        print(f'{self.name} ({self.__class__}) quack quack!')

class MallardDuck(Duck):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f'{self.name} ({self.__class__}) is flying well!')

    def quack(self):
        print(f'{self.name} ({self.__class__}) coin coin!')

if __name__ == '__main__':
    duck1 = NormandyDuck('donald')
    duck1.fly()
    duck1.quack()
    picsou = MallardDuck('picsou')
    picsou.fly()
    picsou.quack()