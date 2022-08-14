class Person:
    def __init__(sk, name, surname, email_id, DoB):
        sk.name = name
        sk.surname = surname
        sk.email_id = email_id
        sk.DoB = DoB

    def age(self, current_year):
        return current_year-self.DoB

anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994,)
pk = Person("pawan", "kumar", "pawanarya93@gmail.com", 1994)
print(pk.name)
print(anuj_var.surname)
print(anuj_var.email_id)
print(anuj_var.DoB)
print(pk.name +  pk.surname)

print(pk.age)
