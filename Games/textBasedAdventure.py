weapon = False

def showSkeletons():
	directions = ["left","backward","forward"]
	global weapon
	print("You see a wall of skeletons as you walk into the room. Someone is watching you.")
	userInput = ""
	while userInput not in directions:
		print("Option:left/backward/forward")
		userInput = input()
		if userInput == "left":
			print("You find that this door opens into a wall.You open some of the drywall to discover a knife.")
			weapon = True
		elif userInput == "backward":
			introScene()
		elif userInput == "forward":
			strangeCreature()
		else:
			print("Please choose a valid option .")
def strangeCreature():
	actions = ["fight","flee"]
	global weapon
	print("A strange goul-like creature has appeared. You can either fight or run. What would you do?.")
	userInput = ""
	while userInput not in actions:
		print("Options: flee/fight")
		userInput = input()
		if userInput == "fight":
			if weapon:
				print("You kill the creature with the knife you found earlier.You find the exit")
			else:
				print("The ghost creature has killed you.")
			quit()
		elif userInput == "flee":
			showSkeleton()
		else:
			print("Please choose a valid option.")








def CameraScene():
	directions = ["forward,backward"]
	print("You see a dropped down camera here. Where would you like to go.")
	userInput = ""
	while userInput not in directions:
		print("Option:forward/backward")
		userInput = input()
		if userInput == "forward":
			print("You found it.You made it to exit")
			quit()
		elif userInput == "backward":
			showShadowFigure()
		else:
			print("Please choose a valid option.")
def hauntedRoom():
		directions = ["right","left","backward"]
		userInput = ""
		while userInput not in directions:
			print("Options:right/left/backward")
			userInput = input()
			if userInput == "right":
				print("Multiple ghost like structures start moving towards you.You are killed.")
				quit()
			elif userInput == "left":
				print("You've made it. You've found an exit.")
				quit()
			elif userInput == "backward":
				introScene()
			else:
				print("Please choose a valid option.")




def showShadowFigure():
	directions = ["right","backward"]
	print("You see a shadowy figure at a distance. You are fearful. Where would you like to go.")
	userInput = ""
	while userInput not  in directions:
		print("Options:right/left/backward")
		userInput = input()
		if userInput == "right":
			cameraScene()
		elif userInput == "left":
			print("You find that this door into a wall.")
		elif userInput == "backward":
			introScene()
		else:
			print("Please choose a valid option.")

def introScene():
	directions = ["right","left","forward"]
	print("You are at crossroads.You can go any of the four hallways.Where would you like to go?")
	userInput = ""
	while userInput not in directions:
		print("Options:right/left/forward/backward")
		userInput = input()
		if userInput == "right":
			showSkeletons()
		elif userInput == "left":
			showShadowFigure()
		elif userInput == "forward":
			hauntedRoom()
		elif userInput == "backward":
			print("You find that this door opens into a wall")
		else:
			print("Please choose a valid option.")








if __name__    == "__main__":
	while True:
		print("Welcome to the Adventure Game!")
		print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
		print("However, during your exploration, you find yourself lost.")
		print("You can choose to walk in multiple directions to find a way out.")
		print("Let's start with your name: ")
		name = input()
		print("Good luck, " +name+ ".")
		introScene()

