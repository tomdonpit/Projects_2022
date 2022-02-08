# Task 4
def show_balance(balance):
    print("Current Balance: $", str(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: $")
    return balance + float(amount)

def withdraw(balance):
    amount = input("Enter amount to withdraw: $")
    return balance - float(amount)

def log_out(name):
    print("Goodbye,", name + "!")
