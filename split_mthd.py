"""
testing split method
"""
greeting = "good morning kimani"
result = greeting.split()
print(result)
print()

my_str = "i will come to visit you on wednesday, friday and saturday"
result1 = my_str.split(",")
print(result1)
print()

string2 = 'as happy" as a king'
result2 = string2.split('"')
print(result2)

#using dunder to check the runned file
if __name__ == "__main__":
    print("script is being run")

#getting the type of object name only
def get_name(obj):
    print(str(type(obj)).split("'")[1])
school = "gaturi"
get_name(school)

#random str
number = (23, 45)
no_str = [str(n) for n in number]
print(no_str)

