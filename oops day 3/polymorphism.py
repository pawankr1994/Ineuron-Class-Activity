class ineuron:
    def students(self):
        print("students detail")

class class_type:
    def students(self):
        print("class type of students")


def ineuron_external(a):
    a.students()

i = ineuron()
j = class_type()
ineuron_external(i)
ineuron_external(j)

def test(a,b):
    return  a+b
print(test(3,4))
print(test("pawan ", " kumar"))


