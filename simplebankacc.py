class BankAccount:
    def __init__(bank, name, balance):
        bank.name = name
        bank.balance = balance

    def display(bank):
        print(f"{bank.name}: {bank.balance}")
    
    def deposit(bank, amount):
        bank.balance += amount
        print(f"Deposited RM{amount}. New balance: RM{bank.balance}")

    def withdraw(bank, amount):
        if bank.balance < amount:
            print("Insufficient funds!")
        else:
            bank.balance -= amount
            print(f"Withdrew RM{amount}. New balance: RM{bank.balance}")
    
acc1 = BankAccount("Emmanuel", 1200)

acc1.display()
acc1.deposit(500)
acc1.withdraw(1000)
acc1.withdraw(2300)