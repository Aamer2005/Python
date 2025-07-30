def main():
    #print("Enter 1 : Celsius To ->\nEnter exit : TO EXIT")
    choice = input("Enter 1 : Celsius To ->\nEnter exit : TO EXIT\n")

    if(choice=="1"):
        celsius_to()
    elif(choice=="exit"):
        print("Exit!!!")

def celsius_to():
    celsius =  float(input("Enter Celcius : "))
    farenheit = celsius*9/5+(32)
    kelvin = 273.15+celsius
    print("celcius :",celsius,"\nfarenheit :",farenheit,"\nkelvin :",kelvin)
    main()


#main()

#Check Whether the given year is leap year or not

def check_leap_year():
    year = int(input("Enter Year : "))
    if(year%4==0):
        return True
    else:
        return False

print(check_leap_year())