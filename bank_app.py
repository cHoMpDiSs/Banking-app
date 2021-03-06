
class User():
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self): #function to change username
        self.name = input(f"Hello, {self.name} What would you like to change your username to?:")
        print("Hello,", self.name, "your username has been updated.")
        return self.name

    def change_pin(self): #function to change user PIN
        
        pincheck = input("Please enter your PIN:")

        if pincheck == self.pin: #pin validation
            new_pin = input("Please enter your new PIN:") #new pin
            self.pin = new_pin
            print("Pin has been updated.")
            return self.pin  #returning the pin to self.pin
        
        elif pincheck != self.pin:
           print("Sorry Invalid Pin. GOODBYE")
            
        

    def change_password(self): #function to change password
        print("Welcome to Password Reset.")
        password_check = input("Please enter your password first:")
        if password_check == self.password: #pawssword validation
            new_password = input("Enter your New Password:") #new password
            self.password = new_password
            return self.password
        else:
            print("Sorry Invalid Password. Goodbye!")



class Bankuser(User):  #Using inheritence here (unecessary but wanted to showcase and use inheritence). 
                       #could have used just one class. But for readablity and less methods per class.  
                        
    def __init__(self, name, pin, password):

        super().__init__(name, pin, password)

        self.balance = 0

    def show_balance(self):
        balance = str(self.balance)
        new_balance = ['$',balance,"0"]                               # Here is how i added the 
        print(self.name, "has a balance of:", ''.join(new_balance))   # to the dollar amount .00
                                                                      # creating a list and joining
    def deposit(self):
        deposit_amount = float(input(f"Hello {self.name} How much would you like to deposit?"))
        self.balance = self.balance + deposit_amount
        balance = str(self.balance)
        new_balance = ['$',balance, "0"]
        print(self.name, "has deposited", ''.join(new_balance),
              "Your new balance is:", ''.join(new_balance))
        return self.balance

    def withdraw(self):

        withdrawl_amount = float(                               #I added a lot of string/float coversion
            input("How much would you like to withdrawl?:"))    #To use string concatenation 
        self.balance = self.balance - withdrawl_amount
        balance = str(self.balance)
        new_balance = ['$',balance,"0"]
        print(self.name, "has a withdrawn:", withdrawl_amount,
              "Your new balance is:", ''.join(new_balance))
        return self.balance

    def transfer_money(self, user): #Using "user" parameter to transfer
        transfer_amount = str(input("How Much Would You Like To Transfer?:"))
        transfer = ['$',transfer_amount,".00"]
        print("You are transferring", ''.join(transfer), "to", user.name)
        print("Authentication Required")
        pin_validation = (input("Please Enter Your PIN:"))

        if pin_validation == self.pin: #pin validation for transfer
            print("Transfer Authorized")
            transfer_amount = float(transfer_amount)
            self.balance = self.balance - transfer_amount
            balance = str(self.balance)
            new_balance = ['$',balance,"0"]
            transfer_amount =str(transfer_amount)
            transfer_amount2 = ['$',transfer_amount,"0"]
            print(self.name, "You have transferred:", ''.join(transfer_amount2), "to", user.name,
                  "Your new balance is:", ''.join(new_balance))
            transfer_amount = float(transfer_amount)
            user.balance = user.balance + transfer_amount

        elif pin_validation != self.pin:
            print("Invalid PIN. Transaction canceled")
     

    def request_money(self, user): #Using "user" parameter to request money
        print("This is the money request function:")
        pin_validation = (input(f"Please enter {user.name}'s PIN:"))

        if pin_validation == user.pin:                  #Pin validation for transfer
            password_validation = input("Please enter your password:")
            if password_validation == self.password:    #Password Validation
                amount_to_transfer = float(
                    input("How much would you like to request:"))
                self.balance = self.balance + amount_to_transfer
                new_balance =  ['$',str(self.balance),"0"]  #Good way to add $ .00 after balance amount
                print("Transfer Succesfull, Your New Balance is:",
                      ''.join(new_balance))
                return self.balance
            else:
                print("Incorrect Password GoodBye!")
        else:
            print("Invalid PIN. Transaction canceled")
        user_balance = ['$', user.balance, "0"]
        print(self.name, " has a balance of", ''.join(new_balance))
        print(user.name, "has a balance of",''.join(user_balance))



"""Driver Code For Program"""
"""I made the program to run interactively for easier check for functionality"""
"""Hope you enjoy :) """
print("***********************************************")
print("***********************************************")
print("******Hello and welcome to bank of Jordon******")
print("***********************************************")
print("***********************************************")

user1_name = input("Please Enter your name to register:")
user1_password = input("Please provide a password:")
user1_pin = input("Please provide a 4 digit PIN:")

user1 = Bankuser(user1_name, user1_pin, user1_password)
user2 = Bankuser("RichPerson", "0000", "password")
while True:

    print("***********************************************")
    print("******1.Deposit***********2.Check Balance******")
    print("***********************************************")
    print("******3.Transfer**********4.Request Money******")
    print("******************5.Exit***********************")
    print("***********************************************")
    user_selection = input(f"What would you like to do {user1.name}?")
    
    if user_selection == "1":
        user1.deposit()

    if user_selection == "2":
        user1.show_balance()

    if user_selection == "3":
        print("Default user info is Name: RichPerson, PIN: 0000, Password: password")
        user1.transfer_money(user2)

    if user_selection == "4":
        print("Default user info is Name: RichPerson, PIN: 0000, Password: password")
        user1.request_money(user2)

    if user_selection == "5":
        print("Goodbye!")
        break
