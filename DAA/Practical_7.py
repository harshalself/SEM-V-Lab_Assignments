# Size of the chessboard (N x N)
N = 8

# Function to print the solution board
def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")  # Print 'Q' for a Queen
            else:
                print(".", end=" ")  # Print '.' for an empty space
        print()

# Recursive function to solve the N-Queens problem
def solveNQueens(board, col):
    # Base case: If all queens are placed, print the solution
    if col == N:
        printSolution(board)
        return True
    
    # Try placing a queen in all rows one by one in the current column
    for i in range(N):
        # Check if placing a queen at board[i][col] is safe
        if isSafe(board, i, col):
            # Place the queen
            board[i][col] = 1
            # Recur to place the rest of the queens
            if solveNQueens(board, col + 1):
                return True
            # If placing queen in board[i][col] leads to a solution, backtrack
            board[i][col] = 0
    
    # If the queen cannot be placed in any row in this column, return False
    return False

# Function to check if placing a queen on board[row][col] is safe
def isSafe(board, row, col):
    # Check the row on the left side
    for x in range(col):
        if board[row][x] == 1:
            return False

    # Check the upper diagonal on the left side
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    # Check the lower diagonal on the left side
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True

# Initialize the board with 0s (0 means no queen is placed)
board = [[0 for x in range(N)] for y in range(N)]

# Start solving the problem from the first column
if not solveNQueens(board, 0):
    print("No solution found")
