
# S'assurer qu'une classe a une seule et unique instance et est accessible depuis n'importe où.

class School:
    def __init__(self, name = None):
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
    school2 = School('school1')
    assert school1 == school2