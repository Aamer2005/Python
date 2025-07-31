print("Welcome To SBI")

class Account:
    def __init__(self):
        self.pincode = ""
        self.balance = 0
        self.menu()

    def menu(self):
        choice = int(input("""
        Enter 1 : Create pincode 
        Enter 2 : Check Balance
        Enter 3 : Deposit 
        Enter 4 : Withdrawl
        """))

        if choice==1 :
            self.create_pin()
        elif choice==2 : 
            self.check_balance()
        elif choice==3 : 
            self.deposit()
        elif choice==4:
            self.withdrawl()
        else:
            print("Logout")

    def create_pin(self):
        self.pincode = input("Enter PinCode : ")

        if self.pincode!="":
            print("Pin Generate Succefully !!!")
        else :
            print("Error in Generation of Pin ! Try Again")

        self.menu()

    def check_balance(self):
        pincode = input("Enter pin : ")
        if pincode == self.pincode:
            print("Balance :",self.balance)
        else :
            print("Wrong pin code!!!")
        self.menu()


    def deposit(self):
        pincode = input("Enter pin : ")
        if pincode == self.pincode:
            amount = int(input("Enter Amount To Deposit : "))
            if amount>=0:
                self.balance=self.balance+amount
                print(" Amount is Deposited")
            else:
                print("Enter A Valid Amount!!!")
        else :
            print("Invalid Pincode !!!")
        self.menu()

    def withdrawl(self):
        pincode = input("Enter pin : ")
        if pincode == self.pincode:
            amount = int(input("Enter Amount to be withdraw : "))
            if self.balance>amount :
                self.balance=self.balance-amount
                print(amount," is withdrawl")
            else:
                print("Not enough balance!!!")
        else :
            print("Invalid Pincode !!!")
        self.menu()

    def exit(self):
        pass


#Object Creation

acc = Account()