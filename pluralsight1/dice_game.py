import random

def roll_dice():
    return random.randint(1,6) + random.randint(1,6)

def main():
    player1 = input("enter the name of the player1: ")
    player2 = input("enter the name of the player2: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1>roll2:
        print(player1, 'WINS!!!')
    elif roll1<roll2:
        print(player2, 'WINS!!!')
    else:
        print('PLAYERS TIED!')

main()