print("Welcome To Code!!!")

def calculateInterest():
    principal = int(input("Enter the Principal Amount : "))
    rate = int(input("Enter the Rate : "))
    Time = int(input("Enter the year : "))

    result = (principal*rate*Time)/100

    print("result : ",result)

calculateInterest()