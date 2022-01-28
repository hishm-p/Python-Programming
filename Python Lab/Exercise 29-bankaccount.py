class bank:

    def __init__(self,accno,name,acctype,bal):
        self.ano = accno
        self.name = name
        self.acct = acctype
        self.balance = bal

    def deposit(self):
        depo = int(input("\nEnter the amount to deposit: "))
        self.balance += depo
        print("Rs.",depo,"is credited to your account\nAVAILABLE BALANCE IS:",self.balance)

    def withdraw(self):
        draw = int(input("\nEnter the amount to withdraw: "))
        self.balance -= draw
        print("Rs.",draw,"is debited from your account\nAVAILABLE BALANCE IS:",self.balance)

    def display(self):
        print("\nACCOUNT DETAILS")
        print("----------------")
        print("Account Number:",self.ano)
        print("Account Holder Name:",self.name)
        print("Account Type:",self.acct)
        print("Available Balance:",self.balance)
        print(" ")

print("\nENTER BANK ACCOUNT DETAILS")
print("--------------------------\n")
accno = int(input("ENTER THE ACCOUNT NUMBER:"))
username = input("ENTER ACCOUNT HOLDER NAME:").title()
acct = input("ENTER THE ACCOUNT TYPE(CURRENT/SAVINGS):").upper()
balance = int(input("ENTER THE CURRENT BALANCE:\n"))

ob = bank(accno,username,acct,balance)

while(1):
    
    print("\nChoose your desired operation:")    
    ch = int(input("1.DEPOSIT\n2.WITHDRAW\n3.VIEW ACCOUNT DETAILS\n4.EXIT\n"))
    if ch == 1:
        ob.deposit()
    elif ch == 2:
        ob.withdraw()
    elif ch == 3:
        ob.display()
    elif ch == 4:
        print("EXIT.")
        exit()
    else:
        print("Invalid Input") 
