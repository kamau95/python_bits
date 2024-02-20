class School:
    """"parent class"""
    def __init__(self, location = ""):
        self.location = location
obj = School()

def check_members(obj,School):
    if type(obj) == School:
        print("am happy u are a member")
check_members(obj, School)

print(type(obj))
