class School:
    
    # dunder => double underscore

    def __init__(self, name = None):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 2:
            self.__name = name
        else:
            print('Unable to update name, too short')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name = name
        else:
            print('Unable to update name, too short')
    
class Hexagone(School):

    def __init__(self):
        super().__init__('hexagone')

class Usvq(School):

    def __init__(self):
        super().__init__('usvq')

hexagone = Hexagone()
usvq = Usvq()

print(f'Hexagone: {hexagone.get_name()}')
#hexagone.get_name() = 'pas hexagone'
hexagone.set_name('pas hexagone')
hexagone.set_name('h')
print(f'Hexagone: {hexagone.name}')
print(f'USVQ: {usvq.get_name()}')
usvq.name = 'pas usvq'
usvq.name = 'u'
print(f'USVQ: {usvq.get_name()}')
