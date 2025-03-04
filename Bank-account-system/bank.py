class BankAccount(object):
	"""docstring for BankAccount"""
	def __init__(self, balance=0):
		self.balance = balance

	def deposit(self,amount):
		if amount>0:
			self.balance += amount
			print(f"deposit ${amount}")

	def withdraw(self,amount):
		if amount>0 and self.balance>=amount:
			self.balance-=amount
			print(f"withdraw ${amount}")

class SavingAccount(BankAccount):
	def apply_interest(self,rate=0.01):
		interest=self.balance*rate
		self.deposit(interest)
		print(f" interest added: ${interest}")

def bank_main():
	acc=SavingAccount()
	while True:
		print("\n1.Deposti \n2. Withdraw \n3. interest \n4. Exit")
		choice=input("Enter Choice : ")
		if choice == '1':
			acc.deposit(float(input("Amount: ")))
		elif choice == '2':
			acc.withdraw(float(input("Amount: ")))
		elif choice == '3':
			acc.apply_interest()
		elif choice == '4':
			break
		else:
			print("invalid choice")
		
bank_main()