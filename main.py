rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
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
import random

chooseHand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computersChoose = 0

if chooseHand == 0:
  print(rock)
elif chooseHand == 1:
  print(paper)
elif chooseHand == 2:
  print(scissors)
else:
  print("Wrong command. Please choose between 0, 1 or 2.")



computersChoose = random.randint(0, 2)

if chooseHand == 0 or chooseHand == 1 or chooseHand == 2:
  print("Computer chose:")
  if computersChoose == 0:
    print(rock)
  elif computersChoose == 1:
    print(paper)
  elif computersChoose == 2:
    print(scissors)
else:
  print("☹️")
  

if chooseHand == 0:
  if computersChoose == 0:
    print("You tied. Try again!")
  elif computersChoose == 1:
    print("You win! Congratulations!")
  elif computersChoose == 2:
    print("You win! Congratulations!")
    
elif chooseHand == 1:
  if computersChoose == 0:
    print("You win! Congratulations!")
  elif computersChoose == 1:
    print("You tied! Try again.")
  elif computersChoose ==2:
    print("You loose! Try again!")

elif chooseHand == 2:
  if computersChoose == 0:
    print("You loose! Try again!")
  elif computersChoose == 1:
    print("You win! Congratulations!")
  elif computersChoose == 2:
    print("You tied! Try again!")




