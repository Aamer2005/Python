class AgeException(Exception):
    def __init__(self,age,msg):
        super().__init__(msg)

def checkAge(age):
    try:
        if(age<18):
            raise AgeException(age , "Not Elligible For Vote!!!")
        else:
            print("Elligible For Vote !!!")
    except AgeException as ae:
        print("REASON :",ae)