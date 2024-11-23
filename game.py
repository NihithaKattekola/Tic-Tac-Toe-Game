import math

# Constants for the players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Initialize an empty board
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

# Function to print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check for a win or draw
def check_winner(board):
    # Rows, columns, and diagonals
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    # Check if there's a winning state
    for state in win_states:
        if state[0] == state[1] == state[2] != EMPTY:
            return state[0]
    # Check for a draw
    if any(EMPTY in row for row in board):
        return None  # Game is still going
    return 'Draw'

# Minimax algorithm with optional Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf, use_alpha_beta=True):
    result = check_winner(board)
    if result == AI:
        return 1
    elif result == HUMAN:
        return -1
    elif result == 'Draw':
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, False, alpha, beta, use_alpha_beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    if use_alpha_beta:
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    eval = minimax(board, depth + 1, True, alpha, beta, use_alpha_beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    if use_alpha_beta:
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
        return min_eval

# AI's move
def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = AI

# Human's move
def human_move():
    while True:
        move = input("Enter your move (row and column): ")
        row, col = map(int, move.split())
        if board[row][col] == EMPTY:
            board[row][col] = HUMAN
            break
        else:
            print("Invalid move! Try again.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        # Human move
        human_move()
        print_board(board)
        if check_winner(board):
            break

        # AI move
        ai_move()
        print("AI played:")
        print_board(board)
        if check_winner(board):
            break

    # Display result
    result = check_winner(board)
    if result == HUMAN:
        print("Congratulations! You won!")
    elif result == AI:
        print("AI wins! Better luck next time.")
    else:
        print("It's a draw!")

# Start the game
play_game()
