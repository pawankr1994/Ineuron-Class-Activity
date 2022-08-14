class ineuron:
    def student(self):
        print("print the detail of all the student")
    def achivers(self):
        print("print the list of achiver")
    def hall_of_fame(self):
        print("print everyone from hall of fame")


class ineuron_vision(ineuron):
    def student(self):
        print("these are the filter student list")

iv = ineuron_vision()
iv.student()

#method overwriting inheritance