import math

# Initialize the board
board = [' ' for _ in range(9)]

# Printing the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print(" ")

# Checking for a win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Checking for a draw
def check_draw():
    return ' ' not in board

# Minimax algorithm to determine the best move
def minimax(is_maximizing):
    if check_win('O'):
        return 1
    if check_win('X'):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI making the move using the minimax algorithm
def ai_move():
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Player's  move
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if check_win('X'):
            print("Congratulations! You win!")
            break
        if check_draw():
            print("It's a draw!")
            break

        ai_move()
        print_board()
        if check_win('O'):
            print("AI wins! Better luck next time.")
            break
        if check_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
