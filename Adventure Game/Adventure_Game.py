print(f"Welcome to my course project. This story will be about a young boy going to summer camp for the first time. ")
print(f"Before this story begins, we need to answer a few questions. ")
print(f"Make sure to press enter after typing each answer. ")
input(f"\nPress the enter key to continue...")
playAgain = "yes"
while playAgain.lower() == "yes":
#Question 1
	subjectClass = input("\nWhat is your favorite subject to study: ")
	while len(subjectClass) == 0:
		subjectClass = input(f"Please enter a subject:  ")
#Question 2
	songChoice = input("\nDo you have a favorite skit or song: ")
	while len(songChoice) == 0:
		songChoice = input(f"Please enter a song or skit:  ")
#Question 3    
	carColor = input("\nWhat color is the car you drive: ")
	while len(carColor) == 0:
		carColor = input(f"Please enter a color:  ")
#Question 4
	scoutName = input("\nWhat is the name of our scout: ")
	while len(scoutName) == 0:
		scoutName = input(f"please enter a name:  ")
#Question 5
	carName = input("\nWhat car do you drive: ")
	while len(carName) == 0:
		carName = input(f"Please enter a car make/model:  ")
		
	print(f"\nOur story begins on a car ride to Camp Olmsted")
	print(f"\n{scoutName} and his friends are playing I Spy on the car ride")
	print(f"'I Spy with my little eye something {carColor}' says {scoutName}'s friend")
	print(f"{scoutName} scans the roads for a bit before spotting a {carColor} {carName}")
	print(f"After the long car ride, {scoutName} and his troop arrive at beautiful Camp Olmsted!")
	print(f"{scoutName} and his troop work together to set up camp and decide to have a camp fire that night")
	print(f"The trooop leader asks if anybody wants to perform a skit or song at the fire")
	skitYesorNo = input(f"\nShould {scoutName} perform a skit or song? Type yes or no:  ")
	while skitYesorNo.lower() != "yes" and skitYesorNo.lower() != "no":
		skitYesorNo = input ("Please type yes or no:  ")
	if skitYesorNo == "yes":
		print(f"\n{scoutName} is very nervous about performing but decides to have a bit of fun")
		print(f"\n{scoutName} performs his favorite skit/song called {songChoice}")
		print(f"The troop has a great time at the fire and {scoutName}'s performance is a hit!")
	else:
		print(f"{scoutName} watches his troop perform various skits and songs")
		print(f"He has a fun time watching and takes notes on his favorite performances")
		print(f"{scoutName} tells himself he will definitely perform next time there is a fire")
	print(f"The next day all the troop members start attending their merit badge classes")
	print(f"Danny has quite a few classes this week but his favorite one is {subjectClass}, its so much fun!")
	print(f"Later on that day it's quite hot and there is opportunities for free time after classes")
	goSwimming = input(f"\n'Hey {scoutName} wanna go swimming in the lake?' his troop members ask. Type yes or no:  ")
	while goSwimming.lower() != "yes" and goSwimming.lower() != "no":
		goSwimming = input("Please type yes or no:  ")
	if goSwimming == "yes":
		print(f"{scoutName} and his troop mates go for a swim on the hot day")
		print(f"{scoutName}'s troop mates have a swimming race but he cannot keep up with them")
		print(f"A fellow troop mate shows {scoutName} how to do a faster stroke so he can keep up")
	else:
		print(f"{scoutName} decides against going to the lake")
		print(f"he instead decides to study for his merit badge classes")
		print(f"{scoutName} is more excited to go to his {subjectClass} class tomorrow anyways")
	if skitYesorNo == "yes" and goSwimming == "yes":
		print(f"The rest of the week goes great and {scoutName} learns a lot in his classes.")
		print(f"When he returns home he has many fun stories to tell his parents")
		print(f"He can't wait to go back next year!")
	elif skitYesorNo == "no" and goSwimming == "no":
		print(f"Despite not participating in a lot of activities, {scoutName} still learns a lot from his classes")
		print(f"When he goes home, he shows his parents all of the merit badges he earned")
		print(f"{scoutName} is happy about all the badges he earned but wishes he had done more with his friends")
	elif skitYesorNo == "yes" and goSwimming == "no":
		print(f"{scoutName} returns home and tells his parents about the fun skit he performed at the fire")
		print(f"{scoutName} also has a lot of merit badges to show off to his parents")
	else:
		print(f"{scoutName} returns home and demonstrates the new swimming stroke he learned")
		print(f"He also has plans to perform a skit at the next campfire they have")
	print("\nThe End")

	playAgain = input(f"\n Do you want to play again? Enter yes or no:  ")
	while playAgain.lower() != "yes" and playAgain.lower() != "no":
		playAgain = input(f"Please type yes or no:  ")