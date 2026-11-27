class BankAccount:
    bank_name = "SBI bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance or invalid amount")

    def display(self):
        print(self.owner, self.balance, self.bank_name)

    @classmethod
    def change_bank(cls, new_name):
        cls.bank_name = new_name

a1 = BankAccount("Nanda",200000)
a2 = BankAccount("Kishore",200000)

a1.deposit(1000)
a2.withdraw(1000)
a1.change_bank("HDFC")
a2.change_bank("Kotak")

a1.display()
a2.display()