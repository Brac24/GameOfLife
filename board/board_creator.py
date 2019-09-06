import random
from cell.cell import Cell

def randomstate(rows, cols):
    #list comprehension to generate a list of lists with random 1's and 0's
    #We can think of this nested list comprehension in terms of nested for loops
    #In nested for loops the inner loop can be considered the column and the outer loop the row
    #Same applies here where the inner list comprehension referes to the column and the outer refers to the row
    board = [[1 if random.random() >= .94 else 0 for col in range(cols)] for row in range(rows)]

    return board

def render(board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        line = ''
        for col in range(cols):
            if board[row][col] is 1:
                line += 'c'
            else:
                line += ' '
        
        print(line)

def render_world(cell_board):
    rows = len(cell_board)
    cols = len(cell_board[0])
    for row in range(rows):
        line = ''
        for col in range(cols):
            cell = cell_board[row][col]
            if cell.alive:
                line += '0'
            else:
                line += ' '
        
        print(line)


if __name__ == '__main__':
    board_random = randomstate(10,70)
    render(board_random)

    