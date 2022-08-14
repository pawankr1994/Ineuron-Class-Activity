class person:
    def __init__(self, name, surname, yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob       #public

pawan = person('pawan', 'singh', 1994)
print(pawan._name1)              #protected
print(pawan._person__surname1)    #private
