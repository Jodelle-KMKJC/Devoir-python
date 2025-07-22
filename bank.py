class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"depot de {amount} effectuer avec succes. nouveau solde : {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("solde insuffisant. operation annuler")
        else:
            self.balance -= amount
            print(f"retrait du {amount} effectuer avec succes. nouveau solde : {self.balance}")

    def display_balance(self):
        print(f"solde actuel: {self.balance}")

#creer un objet de la classe bankAccount
account = BankAccount("jodelle cabrelle", 1000)

#afficher le solde initial
account.display_balance()

#effectuer un depot
account.deposit(500)

#effectuer un retrait
account.withdraw(200)

#essayer de retirer plusque le solde
account.withdraw(2000)

#afficher le solde final
account.display_balance()