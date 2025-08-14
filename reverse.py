def reverse(number1):
    
    sum=0;number=number1;

    while number>0:
        temp=number%10
        sum = sum*10+temp
        number = int(number/10)

    return sum

def is_equal(number1,number2):
    temp1 = reverse(number1)
    temp2 = reverse(number2)

    if temp1==number2 and temp2==number1:
        return True
    else:
        return False

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

print(reverse(num1))
print(is_equal(num1,num2))