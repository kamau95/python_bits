class Animal:
    #constructor
    def __init__(self, appearance= 'unknown', birthType= 'unknown',\
            bloodType= 'unknown'):
        self.appearance = appearance
        self.birthType = birthType
        self.bloodType = bloodType

    @property
    def apperance(self):
       return self.__appearance

    @apperance.setter
    def apperance(self, appearance):
        self.__apperance = appearance

    @property
    def birthType(self):
       return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def bloodType(self):
        return self.__bloodType

    @bloodType.setter
    def bloodType(self, bloodType):
        self.__bloodType = bloodType

    #method overriding
    def __str__(self):
        print(f"Animal description: {self.apperance}\
                {self.birthType} {self.bloodType}")

class Mammal(Animal):
    #constructor
    def __init__(self, nurseYoung= True):
        Animal.__init__(appearance, birthType, bloodType)
        self.nurseYoung= nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung= nurseYoung

class Reptile(Animal):
    #constructor
    def __init__(self, legs= False):
        Animal.__init__(appearance, birthType, bloodType)
        self.legs = legs

    @property
    def legs(self):
        return self.__legs

    @legs.setter
    def legs(self, legs):
        self.__legs = legs

def main():
    lion = Animal("fur", "gives birth", "warm-blooded")
main()
