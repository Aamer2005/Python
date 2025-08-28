class Division:
    def __init__(self,num1,num2):
        self.num1 = num1;
        self.num2 = num2;
        self.division();

    def division(self):
        result = 0
        try:
            result = self.num1//self.num2
        except Exception:
            print("Division By Zero")
        finally:
            print('quotient' , result)

d = Division(10,0)