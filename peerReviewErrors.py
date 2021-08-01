# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Andrew McDonald
# Creation Date: 07/31/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")

		      
--------------------------------------------------------------------------------------------------
#CORRECTED VERSION
		      
import random
import time 

def displayIntro():
	#Not sure if this is a correction but I brought the text to the front of the line so the message is uniform on each line when displayed (1)
	print('''You are in a land full of dragons. In front of you, 
you see two caves. In one cave, the dragon is friendly 
and will share his treasure with you. The other dragon 
is greedy and hungry, and will eat you on sight.''')
print()
	
def chooseCave():
	cave = ''
	#Corrected unnecessary indention in the next line for the while statement (2)
	while cave != '1' and cave != '2':
		print('Which cave will you into? (1 or 2)')
		cave = input()
	#Corrected the variable error (logical error) to change 'caves' to 'cave' as 'caves' is not defined in this exercise (3)
	return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	# Corrected the time below from time.sleep(3) to time.sleep(2) since the instruction above says sleep 2 seconds (4)
	time.sleep(2)
	print('A large dragon jumps out in front of you! He open his jaws and...')
	print()
	#sleep for 2 seconds 
	time.sleep(2)
	
	friendlyCave = random.randint(1, 2)
	
	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#Corrected the print statement to include parenthesis that were not included (syntax error) (5)
		print('Gobbles you down in one bite!')

#Added 'y' for accepted playAgain input (6)
playAgain = 'yes' and 'y'
# Corrected the conditional statement being '==' instead of '=' (syntax error) (7)
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	# Corrected variable error to now be chooseCave() as choosecave() is not defined (logical error) (8)
	caveNumber = chooseCave()
	checkCave(caveNumber)

	print('Do you want to play again? (yes or no)')
	playAgain = input()
	
# Corrected indention for the if statement (syntax error) (9)
if playAgain == 'no' or playAgain == 'n':
	# Corrected the spelling error of 'planing' to 'playing' (10)
	print('Thanks for playing')
