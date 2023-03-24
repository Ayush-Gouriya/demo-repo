# Simple note taking application in python

import os


def read_nth_line(fileName,n):
	lastLine = " "
	f = open(fileName,'r')
	count = 1
	for l in f:
		if count == n:
			lastLine = l
			break
		count+= 1
	fileLen = len(list(f))
	f.close()
	return [lastLine,fileLen]
	
def menu():
	print(''' Choose an option:
		1. Create a Note.
		2. View Notes
		3. Mark Notes
		4. Quit''')
	noteopt = input()
	if noteopt == "1":
		fileCheck = os.path.isfile("./Incomplete.txt")
		if fileCheck != 1:
			f = open("Incomplete.txt",'a')
			print("Write the note:\n")
			note = input()
			f.write("1. "+note)
			f.close()
			menu()
		else:
			fileName = "Incomplete.txt"
			f = open(fileName,'a')
			print("Write the note:\n")
			note = input()
			i = read_nth_line(fileName,read_nth_line(fileName,1)[1])[0]
			f.write("\n"+str(int(i[0])+1)+ ". " + note)
			f.close()
			menu()
	elif noteopt == "2":
		viewopt = input(''' Choose:
			1. Completed Notes
			2. Incompleted Notes\n''')
		if viewopt == '1':
			f = open("Completed.txt",'r')
			for l in f:
				print(l) 
		elif viewopt == '2':
			fileName = "Incomplete.txt"
			f = open(fileName,'r')
			print("Choose: Mark Complete(y/n: )")
			markComplete = input()
			if markComplete == 'y':
				for l in f:
					print(l) 
					print("--------------------------------------------------------------------------")
				index = input("Enter the task to mark complete: ")
				fNewName = "Completed.txt"
				fNew = open(fNewName,'a')
				fNew.write(read_nth_line(fileName,index)[0])
				fNew.close()
			elif markComplete == 'n':
				f.close()
				menu()
			else:
				print("Enter correct choice")
				f.close()
				menu()
			f.close()
			menu()


		else:
			menu()
		menu()
	elif noteopt == "4":
		return 0
menu()