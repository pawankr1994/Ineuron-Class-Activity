class person1:
    _name = "pawan"
    __surname = "kumar"
    yob = 1994
    def _age(self, current_year):
        return current_year - self.yob
    def __age1(self, current_year):
        return current_year - self.yob
obj = person1()
print(obj._age(2022))
print(obj._person1__age1(2021))


class employee(person1):
    _name = 'aryan'
    __surname = 'raj'
    yob = 1995
obj1 = employee()
print(obj1._age(2020))
print(obj1._person1__age1(2019))
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._employee__surname)

