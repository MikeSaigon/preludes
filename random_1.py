import random
import time
# coin = random.randint(1,2)

# myselection = input("Do you want heads or tails\n").lower()

# print(f"You have selected '{myselection}'")

# time.sleep(4)

# if myselection == "heads":
#     mychoice = 1
# elif myselection == "tails":
#     mychoice = 2
# else:
#     mychoice = 3
#     print("You have entered an invalid selection")
    
# if mychoice == coin:
#     print(f"The answer was {myselection} You Won")
# else:
#     print(f'The answer was not " {myselection} " Please try again') 

# states_of_america = ["Delaware","Pennsylvania","Maine","Vermont","New Hampshire"]
# provinces_and_territories = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 
#                             'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island', 
#                             'Quebec', 'Saskatchewan', 'Yukon']

# montreal_canadiens_1955 = ['Jean Beliveau', 'Dickie Moore', 'Bernie Geoffrion', 'Maurice Richard', 'Henri Richard',
#                            'Bert Olmstead', 'Doug Harvey', 'Tom Johnson', 'Dollard St. Laurent', 'Bob Turner',
#                            'Jacques Plante']

# montreal_canadiens_1955.insert(0,'Mike Emblem')

# Import the random module here

# Import the random module here

# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
# x=len(names)
# number=random.randint(0, x - 1)
# #Write your code below this line 👇
# print(f"{names[number]} will be paying the bill tonight")

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# tcol=int(position[0])
# trow=int(position[1])

# x = tcol - 1
# y = trow - 1

# if y == 0:
#     row1[x] = " X"
# elif y == 1:
#     row2[x] = " X"
# else:
#     row3[x] = " X"


# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
banner = '''

    PRESENTING THE ROCK PAPER SCISSORS CHALLENGE

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
playerA=input("Rock, Paper, Scissors!").lower()

print(banner) 

print("My Hand")

if  playerA == "rock":
    print(rock)
elif playerA == "scissors":
    print(scissors)
else:
    print(paper)

print("Computer's Hand")
computer = random.randint(1,3)
if computer==1:
    print(rock)
if computer==2:
    print(paper)
if computer==3:
    print(scissors)


if  computer == 1 and playerA =="rock":
    print("Tie Game.  Try again")
elif computer == 2 and playerA == "rock":
    print("Computer wins")
elif computer == 3 and playerA == "rock":
    print("You win")
elif computer == 1 and playerA =="paper":
    print("You win.  ")
elif computer == 2 and playerA == "paper":
    print("Tie Game!")
elif computer == 3 and playerA == "paper":
    print("Computer Wins")  
elif computer == 1 and playerA =="scissors":
    print("Computer wins.  ")
elif computer == 2 and playerA == "scissors":
    print("You Win!")
elif computer == 3 and playerA == "scissors":
    print("Tie game")  
else:
    print("Your choice was not vaiid.  Please try again.")
