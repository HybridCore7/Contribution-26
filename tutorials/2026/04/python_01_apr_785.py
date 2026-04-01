import random

def solve_sudoku(board):
    # Find an empty cell to start with
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return fill_empty(board, i, j)

def fill_empty(board, row, col):
    # Try numbers from 1 to 9
    for num in range(1, 10):
        # Check if number can be placed at this position
        if is_valid(board, row, col, num):
            # Place the number on the board
            board[row][col] = num
            
            # If all numbers have been tried and a solution has been found
            if fill_empty(board, row + 1, col) == False:
                # Backtrack by removing the last number placed
                board[row][col] = 0
                
                return True

    # If no valid number can be placed at this position, backtrack and try next cell
    return False

def is_valid(board, row, col, num):
    # Check if the same number already exists in the row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    # Check the 3x3 box that contains this cell
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
                
    # If the number is valid, continue with the next cell
    return True

# Create an empty Sudoku board
board = [[0]*9 for _ in range(9)]

# Randomly fill some cells with numbers
for i in range(10):
    row = random.randint(0, 8)
    col = random.randint(0, 8)
    board[row][col] = i + 1

# Solve the Sudoku puzzle using recursive backtracking
solve_sudoku(board)

# Print the solved Sudoku puzzle
for row in board:
    print(row)