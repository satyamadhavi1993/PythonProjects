import random

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


items = ['Rock', 'Paper', 'Scissors']
items2 = [rock, paper, scissors]
user_selection = ''
while True:
    try:
        user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
        break
    except:
        print('Please enter a valid number between (0, 1, 2).')

if user_selection < 0 or user_selection > 2:
    print('You lose.')
    exit(0)
print(f'You Selected \n {items2[user_selection]}')
computer_selection = random.randint(0, 2)
print(f'Computer Selected \n {items2[computer_selection]}')
user_selection = items[user_selection]
computer_selection = items[computer_selection]

if ((user_selection == 'Rock' and computer_selection == 'Scissors') or
        (user_selection == 'Scissors' and computer_selection == 'Paper') or
        (user_selection == 'Paper' and computer_selection == 'Rock')):
    print("\nYay!! You won !")
elif user_selection == computer_selection:
    print("\nIts a draw. Please try again.")
else:
    print("\nSorry, Computer won. Better luck next time.")
