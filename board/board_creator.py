import random

def deadstate(rows, cols):
    board = []
    
    #add the row of zeros to the board
    for row in range(rows):
        deadrow = []
        for col in range(cols):
            deadrow.append(0)
        board.append(deadrow)
    
    return board

def randomstate(rows, cols):
    board = deadstate(rows, cols)
    for row in range(rows):
        for col in range(cols):
            value = random.random()
            if(value >= .9):
                board[row][col] = 1
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

if __name__ == '__main__':
    board = deadstate(2,3)
    board_random = randomstate(10,70)
    render(board_random)

    