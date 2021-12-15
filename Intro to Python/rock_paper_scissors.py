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

game_images = [rock, paper, scissors]

choose = int(input('Press 0 for Rock, 1 for Paper and 2 for Scissors\n'))
if choose >=3 or choose < 0:
    print('Invalid digit, You lose')
else:
    print(game_images[choose])
        
            
    comp = random.randint(0, 2)
    print('Computer choose:')

    print(game_images[comp])




    if choose == 0 and comp == 2:
        print(f'{game_images[choose]}\nYou Win')
    elif comp == 0 and choose == 2:
        print(f'{game_images[choose]}\nYou lose')
    elif comp > choose:
        print('You lose')
    elif choose < comp:
        print('You Win')

    elif choose == 2 and comp == 1:
        print(f'{game_images[choose]}\nYou win')
    elif comp == 2 and choose == 1:
        print(f'{game_images[choose]}\nYou lose')

    elif choose == 1 and comp == 0:
        print(f'{game_images[choose]}You win')
    elif comp == 1 and choose == 0:
        print(f'{game_images[choose]}You lose')

    elif comp == choose:
        print('It is a Draw')

