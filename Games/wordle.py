for guess_no in range(6):
	guess = input(f"Guess_{guess_no}: ")
	if guess == "SNAKE":
		print("Correct")
		break
	else:
		print("Wrong")