filename = 'programming.txt'

 with open(filename) as f_obj:
 	professor=input("Enter your qalification: ")
 	f_obj.write(professor)
 	contents = f_obj.read()
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")