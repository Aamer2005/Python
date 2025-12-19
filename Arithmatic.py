class _Account(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def calculate(self):
        self.x =  self.a**self.b
    
    def __repr__(self):
        return f"{self.a}^{self.b} = {self.x}"

class Pattern:
    size = 3
    
    @classmethod
    def right_triangle(cls):
        size = cls.size
        
        for line in range(1,size+1):
            spaces = size-line
            for space in range(1,spaces+1):
                print(" ",end='')
            for star in range(1,line+1):
                print('*',end='')
                
            print()

Pattern.size = 4
Pattern.right_triangle()