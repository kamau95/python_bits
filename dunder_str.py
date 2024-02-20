"""
a class that illustrates how a simple home can\
        be represented using __str__ and other methods
"""
class Home:
    #constructor
    def __init__(self, name = "unknown", rooms = "unknown",\
            has_farm = True, kitchens = "unknown"):
        self.name = name
        self.rooms = rooms
        self.has_farm = has_farm
        self.kitchens = kitchens

    def __str__(self):
        """ this method takes no parameters """
        return "{} home has {} rooms {} garden and {} cooking areas"\
                .format(self.name,\
                self.rooms, self.has_farm, self.kitchens)

home1 = Home("Julia's", 12, False, 3)
print(home1)
print("------------------------------------------")
print(home1.__str__())
print("------------------------------------------")
print(str(home1))
print("------------------------------------------")
print(home1.__repr__())
print("------------------------------------------")
print(repr(home1))
print()
