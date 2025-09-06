import random

num = random.randint(1,100)
print(num) 

guess = 0

count =0

while guess!=num:
    count+=1
    guess = int(input('Enter number : '))
    if guess>num :
        print("Guess Lower Number")
    elif guess<num:
        print("Guess Higher Number")
    elif guess==num :
        print("Write number")
        break

print("Trials :",count)