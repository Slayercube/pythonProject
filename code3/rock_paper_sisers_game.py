import random
while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper or scissors?: ').lower()

    if player == computer:
        print('Computer: ', computer)
        print('Player: ', player)
        print('It\'s a tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You lose!')
        if computer == 'scissors':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You win!')

    elif player == 'paper':
        if computer == 'rock':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You win!')
        if computer == 'scissors':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You lose!')

    elif player == 'scissors':
        if computer == 'rock':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You lose!')
        if computer == 'paper':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You win!')

    play_again = input('Play again? (yes/no): ').lower()
    if play_again != 'yes':
        break

print('Bye!')
