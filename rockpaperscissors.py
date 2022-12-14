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


player_choice = int(input('Type:\n "0" for choosing a Rock\n "1" for Paper\n"2" for Scissors:\n'))

game_images = [rock, paper, scissors]
if player_choice >= 3 or player_choice <= 0:
    print('You have choose invalid number, You lost!')
else:
    print(game_images[player_choice])

    computer_choice = random.randint(0, 2)
    print('Computer chose:')
    print(game_images[computer_choice])

    if player_choice == computer_choice:
        print('A draw!')

    elif computer_choice == 0:
        if player_choice == 1:
            print('You won')
        else:
            print('You loose')
    elif computer_choice == 1:
        if player_choice == 0:
            print('You loose')
        else:
            print('You won')

    elif computer_choice == 2:
        if player_choice == 0:
            print('You won')
        else:
            print('You loose')




