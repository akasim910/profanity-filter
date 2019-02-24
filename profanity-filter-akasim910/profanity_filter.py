def main():
	file = open("bad-words.txt", 'r')
	row = file.readlines()
	for line in row:
		print(line)





if __name__ == '__main__':
	main()