# Tic-Tac-Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to print the game board
def print_board():
    print('---------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('---------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('---------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('---------')

# Function to check if there is a winner
def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True, board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True, board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True, board[0]
    if board[2] == board[4] == board[6] != ' ':
        return True, board[2]

    # No winner
    return False, ''

# Function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    player = 'X'

    while True:
        position = int(input(f"Player {player}, choose a position (1-9): ")) - 1

        if position < 0 or position >= 9 or board[position] != ' ':
            print("Invalid move. Try again.")
            continue

        board[position] = player
        print_board()

        winner, symbol = check_winner(board)
        if winner:
            print(f"Player {symbol} wins!")
            break

        if ' ' not in board:
            print("It's a tie!")
            break

        # Switch players
        player = 'O' if player == 'X' else 'X'

# Start the game
play_game()

