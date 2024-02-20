class Locomotive:
    """type of vehicles"""
    num_vehicles = 0



    def __init__(self, make,cc):
        self.typ =  make
        self.cc = cc

toyota = Locomotive("premio", 1200)

class Bike(Locomotive):
    num_bikes = 0
    
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower


def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
      

bike_instance = Bike("Honda", 175)
print(is_kind_of_class(bike_instance, Bike))
print(is_kind_of_class(toyota, Locomotive))
