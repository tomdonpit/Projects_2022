from banking_pkg import account

# ATM Menu Fn
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Task 2
# Registration
print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0

#Starting balance
print("Name is: ", name)
print("PIN is: ", pin)
print(name, "has been registered with a starting balance of $" + str(balance))

# Task 3
# Log-in
while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter user name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

# ATM Menu
while True:
    print("          === Automated Teller Machine ===          ")
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        account.show_balance(balance)
        print("Current Balance: $" + str(balance))
    
    elif option == "2":
        balance = account.deposit(balance)
        print("Current Balance: $" + str(balance))
    
    elif option == "3":
        balance = account.withdraw(balance)
        print("Current Balance: $" + str(balance))
    
    elif option == "4":
        account.log_out(name)
        break
    
    else:
        break