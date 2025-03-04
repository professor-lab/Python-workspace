class calculator:
	def add(self,a,b):
		return a+b
	def sub(self,a,b):
		return a-b
	def mul(self,a,b):
		return a*b
	def div(self,a,b):
		return a/b 

def main():
	cal=calculator()
	while True:
		print("\n1.Addition\n2.subtract\n3.multiply\n4.divided\n5.exit")
		choice=input("enter the your choice :")
		if choice=='5':
			break
		a=float(input("enter No 1 :"))
		b=float(input("enter No 2 :"))
		if choice=='1':
			print("result: ",cal.add(a,b))
		if choice=='2':
			print("result: ",cal.sub(a,b))
		if choice=='3':
			print("result: ",cal.mul(a,b))
		if choice=='4':
			print("result: ",cal.div(a,b))
		else:
			print("invalid choice")
if if __name__ == '__main__':
	main()
		