class person:
    def age(self, current_year, Year_of_birth):
        return current_year-Year_of_birth
    def email_id_input(self,email_id):
        print('take email id', email_id)
    def ask_name(self):
        name = input("tell me your name: ")
        return name
    def ask_DoB(self):
        DoB = input("tell me your Date_of_birth")
        return DoB

pawan= person()
hitesh= person()
gargi= person()

pawan.email_id_input("pawanaryan93@gmail.com")
print(pawan.ask_name())
