
# S'assurer qu'une classe a une seule et unique instance et est accessible depuis n'importe où.

# Solution 2

class SchoolMeta(type):
    
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class School(metaclass=SingletonMeta):
    def __init__(self, name = None):
            self.students = []
            self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name = name
        else:
            print('Unable to update name, too short')

if __name__ == '__main__':
    school1 = School('school1')
    school2 = School('school2')
    school1.students.append('student1')
    school1.students.append('student2')
    print('school1', school1.students)
    print('school2', school2.students)
    print(school1, school2)
    assert school1 == school2