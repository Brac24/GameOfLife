from cell.cell import Cell

class World():
    def __init__(self, board):
        self.world = []
        for row in range(len(board)):
            cells = []
            for col in range(len(board[0])):
                cell = Cell([row, col], board[row][col])
                
                cells.append(cell)
            
            self.world.append(cells) #add row of cells to world


    def cell_at(self, x, y):
        cell = self.world[x][y]
        return cell


       
