import random

rows = 4
cols = 5
board = []
 #add the row of zeros to the board
#This shows a nested list comprehension
board = [[0 for row in range(rows)] for col in range(cols)]

board = [[1 if random.random() >= .9 else 0 for row in range(rows)] for col in range(cols)]


print(board)
    