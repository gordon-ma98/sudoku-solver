
board1 = [
        [1, 0, 7, 4, 8, 3, 0, 6, 5],
        [8, 5, 0, 6, 7, 1, 0, 0, 3],
        [3, 0, 0, 0, 2, 9, 1, 7, 8],
        [4, 0, 3, 2, 0, 6, 7, 0, 0],
        [6, 0, 0, 3, 0, 0, 2, 0, 0],
        [5, 0, 2, 0, 6, 0, 6, 3, 4],
        [7, 1, 0, 9, 5, 2, 3, 0, 0],
        [9, 0, 0, 0, 3, 7, 5, 1, 2],
        [2, 0, 5, 1, 6, 0, 0, 0, 7]
    ]

#---------------------------------------------------------

# Recursively Calls the Function to Search
def sudoku_solve(board):

    # Base Case:
    empty = search_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    # Recusive Case:
    for i in range(1, 10):

        # If Valid
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            #Recusive Call
            if sudoku_solve(board):
                return True

            #Reset the Value and Try Again
            board[row][col] = 0

    return False

#---------------------------------------------------------

# Checks if it is Valid
def is_valid(board, num, pos):

    #Checking the Row:
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #Check the Column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #Check 3x3 Boxes
    x_box = pos[1] // 3 #Gives 0, 1, or 2
    y_box = pos[0] // 3 #Gives 0, 1, or 2
    for i in range(y_box * 3, y_box * 3 + 3):
        for j in range (x_box * 3, x_box * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

#---------------------------------------------------------

#Prints out the Board
def board_print(board):

    # Prints Horizontal Line Every 3 Rows
    for i in range(len(board)):
        if i != 0 and i % 3 == 0:
            print("- - - - - - - - - - - -")

        #Prints a Line Every 3 Digits
        for j in range(len(board[0])):
            if j != 0 and j % 3 == 0:
                print(" | ", end="")

            # Prints Spaces or Not
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#---------------------------------------------------------

# Finds a Position which is Empty
def search_empty(board):

    # i = row, j = column
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i,j

    return None

print("OLD")
board_print(board1)
sudoku_solve(board1)
print("NEW")
board_print(board1)
