from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Flying(Vehicle):
    @abstractmethod
    def fly(self):
        pass

class Aircraft(Flying):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Vehicle):
    def go(self):
        print("Going")

if __name__ == '__main__':
    supercar = Car()
    supercar.go()
    superfly = Aircraft()
    superfly.go()
    superfly.fly()