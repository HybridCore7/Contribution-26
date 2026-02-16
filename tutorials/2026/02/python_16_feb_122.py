import random

def solve_sudoku(board):
    # Find the first empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try numbers 1-9
                for num in range(1, 10):
                    # Check if the number is valid
                    if is_valid(board, i, j, num):
                        # Make a move
                        board[i][j] = num
                        # If the board is solved, return True
                        if is_board_solved(board):
                            return True
                        # Otherwise, backtrack
                        else:
                            # Remove the number from the cell
                            board[i][j] = 0
                return False
    # If no number is valid, return False
    return False

def is_valid(board, row, col, num):
    # Check the row
    for x in range(9):
        if board[row][x] == num:
            return False
    # Check the column
    for x in range(9):
        if board[x][col] == num:
            return False
    # Check the 3x3 box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def is_board_solved(board):
    # Check if the board is full and correct
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
            if not is_valid(board, i, j, board[i][j]):
                return False
    return True

# Initialize the board
board = [[0]*9 for _ in range(9)]

# Fill the board with random numbers
for i in range(9):
    for j in range(9):
        board[i][j] = random.randint(0, 9)

# Solve the puzzle
if solve_sudoku(board):
    # Print the solved board
    for row in board:
        print(row)
else:
    print("No solution exists")