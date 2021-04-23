import random

# Start the Game, Enter Names 
def main():
    playerOne = input('Player One - Please enter username: ')
    print('Greetings! ' + playerOne + '\n')
    playerTwo = input('Player Two - Please enter username: ')
    print('Greetings! ' + playerTwo + '\n')

# Vars for Scoreboard
    p1 = 0 
    wins_p1 = 0
    p2 = 0 
    wins_p2 = 0
    rounds = 1

# Construction for Win/Lose, Round Number
    while rounds != 4: # Never forget how long it took to find that i forgot to write an 's' 
        print('Round ' + str(rounds))
        p1 = dice_roll()
        p2 = dice_roll()
        print(playerOne + ' Rolls: ' + str(p1))
        print(playerTwo + ' Rolls: ' + str(p2))

        if p1 > p2: 
            wins_p1 = wins_p1 + 1
            print(playerOne + ' wins! \n')
        elif p2 > p1: 
            wins_p2 = wins_p2 + 1
            print(playerTwo + ' wins! \n')
        else: 
            print('Draw- Try Again! \n')

        rounds = rounds + 1

# Determine a Winner
    if wins_p1 > wins_p2:
        print(playerOne + ' Wins - Rounds Won: ' + str(wins_p1))
    elif wins_p2 > wins_p1: 
        print(playerTwo + ' Wins - Rounds Won: ' + str(wins_p2))
    else: 
        print('Draw- Try Again! \n')


# Roll the dice!
def dice_roll():
    dice = random.randint(1, 6)
    return dice 

main()