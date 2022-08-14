class Person:
    def __init__(sk, name, surname, email_id, DoB):
        sk.name = name
        sk.surname = surname
        sk.email_id = email_id
        sk.DoB = DoB
    def __init__(sk, name, surname):
        sk.name = name
        sk.surname = surname

    def age(self, current_year):
        return current_year-self.DoB

pk = Person("pawan", "kumar")