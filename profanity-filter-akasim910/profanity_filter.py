def censor_word(temp):
	new_str = ""
	s = ['$','#','@','*','&','%']
	new_str += temp[0]
	for i in range(len(temp) - 2):
		new_str += random.choice(s)
	new_str += temp[-1]
	return new_str
	



def check_if_bad_word(temp):
	file = open("bad-words.txt", 'r') 
	file1 = file.readlines()

	##string that will be looked for
	##if you want to test input

	#temp = input("Enter the word that you want to search: ")

	#add /n to end of string and convert it to a list
	temp += "\n"
	temp = [temp]

	#get any matches
	result = set(file1).intersection(temp)
	result = list(result)

	#set bool value to default
	bool_val = None

	if len(result) > 0:
		print("**************************************")
		print("    YOU HAVE ENTERED A BAD WORD     ")
		print("**************************************")
		#prints what word matches
		print("The bad word is: ")
		print(result[0][:-1])
		bool_val = True
	else:
		print("************************")
		print("    NOT A BAD WORD     ")
		print("************************")
		bool_val = False




if __name__ == '__main__':
	import random
	temp = "ass"
	check_if_bad_word(temp)
	print(censor_word(temp))
