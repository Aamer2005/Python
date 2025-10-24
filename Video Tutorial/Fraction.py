class Fraction:

    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

    def __str__(self):
        return "{}/{}".format(self.number1,self.number2)

    def __add__(self,other):
        number1 = self.number1*other.number2 + (self.number2*other.number1)
        number2 = self.number2*other.number2
        return "{}/{}".format(number1,number2)