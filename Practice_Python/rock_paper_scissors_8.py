"""
Rock, Paper and Scissors

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""


def welcome():

    print(f'{"-"} * 100')
    print(f'\n\t WELCOME TO RPS GAME')
    print(f"""\nRemember the rules:

\n\t- Rock beats scissors
\n\t- Scissors beats paper
\n\t- Paper beats rock""")

    print(f'\n\n\tTO START CHOICE YOUR MOVE:')

def selection(player):
    
    choose = input(f'\n{player} choose your move: ')
    choose = choose.strip().lower()

    return(choose)

def combat(player_1, player_2):
    
    if player_1 == player_2:
        print("It's a draw!")
    elif player_1 == "rock" and player_2 == "scissors":
        print(f"\nPlayer 1 is the winner!")
    elif player_2 == "rock" and player_1 == "scissors":
        print(f"\nPlayer 2 is the winner!")
    elif player_2 == "scissors" and player_1 == "paper":
        print(f"\nPlayer 2 is the winner!")
    elif player_1 == "scissors" and player_2 == "paper":
        print(f"\nPlayer 1 is the winner!")
    elif player_2 == "rock" and player_1 == "paper":
        print(f"\nPlayer 1 is the winner!")
    elif player_2 == "rock" and player_1 == "paper":
        print(f"\nPlayer 1 is the winner!")
    elif player_1 == "rock" and player_2 == "paper":
        print(f"\nPlayer 1 is the winner!")


def goodbye():
    
    play_again = input(f'\n\tWould you like to play again? (Y/N): ').strip().upper()

    if play_again == "Y":
        welcome()
    elif play_again == "N":
        print(f'\n\tThank you for play. Ciao!')
    else:
        print(f'\nThat is not a valid option, try again.')
        goodbye()


    

if __name__ == '__main__':
    welcome()
    player_1 = selection('Player 1')
    player_2 = selection('Player 2')

    combat(player_1, player_2)

    goodbye()