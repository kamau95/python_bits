"""
python class person tat 
has a method that displays a persons information
"""


class Person:
    #constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display_info(self):
        print(self.name, self.id)
rea = Person('kiogora', 12089)
rea.display_info()

class Woman(Person):
    #constructor
    def print_info(self):
        print("woman class called")

ketraco = Woman('mwende', 4563)
ketraco.print_info()
ketraco.display_info()



