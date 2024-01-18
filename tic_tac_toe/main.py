def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(row[i] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_user_move():
    row = int(input("Enter row (1, 2, or 3): ")) - 1
    col = int(input("Enter column (1, 2, or 3): ")) - 1
    return row, col

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = get_user_move()

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            current_player = players[1] if current_player == players[0] else players[0]
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
