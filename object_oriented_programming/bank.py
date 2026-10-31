class BankAccount:
    def __init__(self , name , id_number , amount):
        self.name = name
        self.id_number = id_number
        self.amount = amount

    def activate(self):
        print(f"{self.name} will activate their accounts")

    def deposit(self):
        print(f"This {self.amount} will be deposited to your account number ")

account_number = BankAccount("Cynthia ", 40040143, 3000)
print(account_number.name)
print(account_number.amount)
account_number.activate()