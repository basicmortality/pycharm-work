board = []

for i in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        row = 0
        if row < 6:
            print board
            row = row + 1
        else:
            return