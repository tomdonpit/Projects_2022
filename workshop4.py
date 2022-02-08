class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        print("Your name has been changed to", self.name)

    def change_pin(self, pin):
        self.pin = pin
        print("Your PIN has been changed to", self.pin)

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    
    def show_balance(self):
        print(self.name, "has an account balance of: $", self.balance)
    
    def withdraw(self):
        withdraw_amount = float(input("How much will you withdraw?: $"))
        self.balance -= withdraw_amount
    
    def deposit(self):
        deposit_amount = float(input("How much will you deposit?: $"))
        self.balance += deposit_amount

    def transfer_money(self, recipient):
        self.recipient = recipient

        if int(input("Enter PIN to transfer: ")) == self.pin:
            transfer = float(input("How much would you like to transfer?: $"))
            self.balance -= transfer
            recipient.balance += transfer
            return True
        else:
            print("Wrong PIN.")
            return False
        
    def request_money(self, payee):
        self.payee = payee
        
        if int(input("Enter payee PIN: ")) == payee.pin and input("Enter payee password: ") == payee.password:
            request = float(input("How much would you like to request?: $"))
            self.balance += request
            payee.balance -= request
            return True
        else:
            print("Wrong PIN and/or password.")
            return False

''' Driver Code for Task 1  '''
""" user1 = User("Bob", 1234, "password")
print("User is named -", user1.name, 
"Their PIN is -", user1.pin, 
"Their password is -", user1.password) """

''' Driver Code for Task 2  '''
""" user1 = User("Bob", 1234, "password")
user1.change_name("Phil")
user1.change_pin(4321)
user1.change_password("newpass")
print("User is named -", user1.name, 
"Their PIN is -", user1.pin, 
"Their password is -", user1.password) """

''' Driver Code for Task 3  '''
""" user1 = BankUser("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password, user1.balance) """

''' Driver Code for Task 4  '''
""" user1 = BankUser("Bob", 1234, "password")
user1.show_balance()
user1.deposit()
user1.show_balance()
user1.withdraw()
user1.show_balance() """

''' Driver Code for Task 5  '''
""" user1 = BankUser("Bob", 1234, "bobpwd")
print(user1.name, user1.pin, user1.password, user1.balance)
user1.deposit()
user1.show_balance()

user2 = BankUser("Alice", 4321, "alicepwd")
print(user2.name, user2.pin, user2.password, user2.balance)
user2.deposit()
user2.show_balance()

user1.transfer_money(user2)
user1.show_balance()
user2.show_balance()

user1.request_money(user2)
user1.show_balance()
user2.show_balance() """