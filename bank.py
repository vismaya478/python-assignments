class Bank:

    bank_name = 'HDFC'

    def __init__(self, Holder_name, acc_number, ifsc):
        self.Holder_name = Holder_name
        self.acc_number = acc_number
        self.ifsc = ifsc
        self.balance = 0
    def get_details(self):
        print(f"Bank name :{self.bank_name}")
        print(f"Holder Name : {self.Holder_name}")
        print(f"Account Number : {self.acc_number}")
        print(f"IFSC code : {self.ifsc}")

    def get_balance(self):
        print(f"Balance = {self.balance}")

    def deposit(self, amount):
        if amount<0:
            print("Enter valid amount.")
        else:
            self.balance += amount
            print(f"Amount deposited : {amount}")


    def withdraw(self, amount):
        if amount>self.balance:
            print("insufficient balance..:")
        else:
            self.balance -= amount
            print(f"amount withdrawn: {amount}")

    @classmethod
    def change_bank(cls,name):
        cls.bank_name = name

    @staticmethod
    def add(a,b):
        print(a+b)


alan = Bank('ALAN',3435464636, 'HDFC325')
bank_name = input("Enter name of bank:")
Bank.change_bank(bank_name)
alan.get_details()
alan.deposit(2000)
alan.deposit(-1)
alan.withdraw(1500)
alan.add(2,4)
