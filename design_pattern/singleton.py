
# S'assurer qu'une classe a une seule et unique instance et est accessible depuis n'importe où.

# Solution 1
# Utiliser 1 attribut de classe et 1 méthode de classe 

class School:
    __instance = None
    def __init__(self, name = None):
            self.students = []
            self.__name = name

    @classmethod
    def get_instance(cls, name: str):
        if cls.__instance is None:
            cls.__instance = School(name=name)
        return cls.__instance

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