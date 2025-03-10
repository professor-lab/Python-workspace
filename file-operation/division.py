print("Give Me Two Number: ")
print(" Enter 'Q' to Quit")

while True:
	first_number=input("\n First Number :")
	if first_number=='q':
		break
	second_number=input("\n second_number: ")
	if second_number=='q':
		break
	answer=int(first_number) / int(second_number)
	print('answer',answer)
