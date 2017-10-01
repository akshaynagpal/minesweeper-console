import math
import random

def open_adjacent_cells(visible_board, hidden_board, board_size, player_coordinates):
    i, j = player_coordinates[0],player_coordinates[1]

    # above left
    if i > 0 and j > 0 and hidden_board[i-1][j-1] != '*':
        visible_board[i-1][j-1] = hidden_board[i-1][j-1]
    # above
    if i > 0 and hidden_board[i-1][j] != '*':
        visible_board[i-1][j] = hidden_board[i-1][j]
    # above right
    if i > 0 and j < (board_size-1) and hidden_board[i-1][j+1] != '*':
        visible_board[i-1][j+1] = hidden_board[i-1][j+1]
    # right
    if j < (board_size-1) and hidden_board[i][j+1] != '*':
        visible_board[i][j+1] = hidden_board[i][j+1]
    # below right
    if i < (board_size-1) and j < (board_size-1) and hidden_board[i+1][j+1] != '*':
        visible_board[i+1][j+1] = hidden_board[i+1][j+1]
    # below
    if i < (board_size-1) and hidden_board[i+1][j] != '*':
        visible_board[i+1][j] = hidden_board[i+1][j]
    # below left
    if i < (board_size-1) and j > 0 and hidden_board[i+1][j-1] != '*':
        visible_board[i+1][j-1] = hidden_board[i+1][j-1]
    # left
    if j > 0 and hidden_board[i][j-1] != '*':
        visible_board[i][j-1] = hidden_board[i][j-1]
    return visible_board

def fill_adjacent_mine_numbers(board_with_mines, mine_positions, board_size):
    for mine_position in mine_positions:
        i = mine_position[0]
        j = mine_position[1]

        # above left
        if i > 0 and j > 0 and board_with_mines[i-1][j-1] != '*':
            board_with_mines[i-1][j-1] += 1
        # above
        if i > 0 and board_with_mines[i-1][j] != '*':
            board_with_mines[i-1][j] += 1
        # above right
        if i > 0 and j < (board_size-1) and board_with_mines[i-1][j+1] != '*':
            board_with_mines[i-1][j+1] += 1
        # right
        if j < (board_size-1) and board_with_mines[i][j+1] != '*':
            board_with_mines[i][j+1] += 1
        # below right
        if i < (board_size-1) and j < (board_size-1) and board_with_mines[i+1][j+1] != '*':
            board_with_mines[i+1][j+1] += 1
        # below
        if i < (board_size-1) and board_with_mines[i+1][j] != '*':
            board_with_mines[i+1][j] += 1
        # below left
        if i < (board_size-1) and j > 0 and board_with_mines[i+1][j-1] != '*':
            board_with_mines[i+1][j-1] += 1
        # left
        if j > 0 and board_with_mines[i][j-1] != '*':
            board_with_mines[i][j-1] += 1
    return board_with_mines

def plant_mines(board, num_mines, board_size):
    mine_positions = []
    for mine in range(num_mines):
        x = random.randint(0, board_size-1)
        y = random.randint(0, board_size-1)
        mine_positions.append([x, y])
        hidden_board[x][y] = '*'
    return board, mine_positions

def draw_board(board):
    print '-----------------------------------\n'
    for row in board:
        for col in row:
            print str(col),
        print '\n'
    print '-----------------------------------\n'

# initialize game
board_size = int(raw_input("Enter board size (2-10)"))
difficulty = int(raw_input("Enter difficulty level (1-9)"))
hidden_board = [[0] * board_size for i in range(board_size)]
num_mines = int(math.floor((float(difficulty)/10)*(board_size*board_size)))

print 'planting mines...'
hidden_board, mine_positions = plant_mines(hidden_board, num_mines, board_size)
hidden_board = fill_adjacent_mine_numbers(hidden_board, mine_positions, board_size)

print 'starting game...'
visible_board = [[0] * board_size for i in range(board_size)]

while(True):
    draw_board(visible_board)
    player_coordinates = map(int, raw_input("Enter coordinates to reveal eg. 2,3\n").strip().split(','))
    x, y = player_coordinates[0], player_coordinates[1]
    if hidden_board[x][y] == '*':
        # TODO visible_board = show_all_mines(visible_board, hidden_board, board_size)
        draw_board(hidden_board)
        print "GAME OVER!"
        break
    elif hidden_board[x][y]>0:
        visible_board[x][y] = hidden_board[x][y]
    else:
        visible_board = open_adjacent_cells(visible_board, hidden_board, board_size, player_coordinates)
