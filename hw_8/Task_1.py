import random


choices = {
    'rock': ["scissors", "lizard"],
    'paper': ["rock", "spock"],
    'scissors': ["paper", "lizard"],
    'lizard': ["spock ", "paper"],
    'spock': ["scissors", "rock"],
}

user_player = None
play_again = 'y'

while play_again.lower() == 'y':
    while True:
        try:
            user_player = input("Your choice (rock, paper, scissors, lizard, spock)?: ")
            possible_actions = ["rock", "paper", "scissors", "lizard", "spock"]
            computer_player = random.choice(possible_actions)

            if user_player.lower() in possible_actions:
                print(f"\nPlayer: {user_player} \nComputer: {computer_player}\n")
            elif user_player.lower() not in possible_actions:
                raise ValueError
            break
        except ValueError:
            print(f'Invalid input "{user_player}"')
    if user_player == computer_player:
        print("It's a TIE!")
    elif computer_player in choices[user_player.lower()]:
        print('Player WIN!')
    else:
        print('Computer WIN')

    while True:
        try:
            play_again = input("Play again? (y/n): ")
            if play_again.lower() not in ["y", "n"]:
                raise ValueError
            break
        except ValueError:
            print(f'Invalid input "{play_again}"')
