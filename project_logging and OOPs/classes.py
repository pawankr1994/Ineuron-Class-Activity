class Person:
    def __init__(self, name, surname, email_id, DoB):
        self.name = name
        self.surname = surname
        self.email_id = email_id
        self.DoB = DoB

anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994,)
pk = Person("pawan", "kumar", "pawanarya93@gmail.com", 1994)
print(pk.name)
print(anuj_var.surname)
print(anuj_var.email_id)
print(anuj_var.DoB)
