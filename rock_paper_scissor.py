import random
match random.randint(0,2):
    case [0]:
        computer_choice = 'rock'
    case [1]:
        computer_choice = 'paper'
    case [2]:
        computer_choice = 'scissor'
    case [num]:
        computer_choice = str(num)
    case _:
        computer_choice = 'rock'
player_choice = input("What do you choose? Enter 'rock', 'paper', or 'scissor'")

if(player_choice == computer_choice):
    print("TIE!")
elif(player_choice == 'rock' and computer_choice == 'scissor'):
    print("WIN!")
elif(player_choice == 'paper' and computer_choice == 'rock'):
    print("WIN!")
elif(player_choice == 'scissor' and computer_choice == 'paper'):
    print("WIN!")    
else:
    print("you lose!")