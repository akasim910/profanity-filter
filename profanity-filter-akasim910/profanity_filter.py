def main():
	file = open("bad-words.txt", 'r') 
	file1 = file.readlines()



	#string that will be looked for
	temp = input("Enter the word that you want to search: ")

	#add /n to end of string and convert it to a list
	temp += "\n"
	temp = [temp]


	#get any matches
	result = set(file1).intersection(temp)
	result = list(result)

	if len(result) > 0:
		print("**************************************")
		print("    YOU HAVE ENTERED A BAD WORD     ")
		print("**************************************")
		#prints what word matches
		print("The bad word is: ")
		print(result[0][:-1])
	else:
		print("************************")
		print("    NOT A BAD WORD     ")
		print("************************")


	








if __name__ == '__main__':
	main()