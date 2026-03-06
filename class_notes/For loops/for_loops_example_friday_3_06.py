#This example comes from the checkers project

PLAYER = "P"
SIZE = 8
EMPTY = "."

board = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)] #list comprehension
#print(board)


# Place player pieces (bottom 3 rows)
for r in range(5, 8):
    for c in range(SIZE):
        if (r + c) % 2 == 1:
            board[r][c] = PLAYER
for row in board:
    print(row)