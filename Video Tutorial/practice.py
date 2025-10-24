class A:
    def __init__(self):
        self.Abcd()
    
    def Abcd(self):
        print("Abcd")

class B(A):
    def __init__(self):
        print("B")

    def __str__(self):
        return "Object Of B"
    



obj = B()
print(obj)