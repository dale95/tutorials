file = open("newfile.txt", "w")
file.write("hello world in the new file\n")
file.write("and another line\n")


while True:
	stuff = raw_input ("Enter something, or 'q' to quit: ")
	file.write(stuff+ "\n")
	if stuff == "q":
		break
file.close()

	


