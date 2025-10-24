print("Hello World")

class Student:
    print('Class Object Created')
    count =0
    def fun():
        print("fun() Invoked!!!")

    def __init__(self,name):
        self.name = name
        self.age =0
    
    def get_name(self):
        return self.name

s = Student("abcd")