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

    #As of now this function goes element by element beginning with the first row and updating 
    #each cell object as it traverses the 2D list of cells
    def next_day(self):
        for row in range(len(self.world)):
            for col in range(len(self.world[0])):
                cell = self.cell_at(row, col)
                live_neighbor_count = 0

                #count number of live cell neighbors
                neighbors = cell.get_neighbors()
                for neighbor_location in neighbors:
                    x = neighbor_location[0]
                    y = neighbor_location[1]
                    #make sure the neighbor location we are going to check is within the confines of the board
                    if (x >= 0 and y >= 0) and (x < len(self.world) and y < len(self.world[0])):
                        neighbor_cell = self.cell_at(x, y)

                        if neighbor_cell.alive:
                            live_neighbor_count += 1

                #logic that decides the destiny of a cell
                if live_neighbor_count in [0, 1] and cell.alive:
                    cell.kill()
                elif live_neighbor_count > 3 and cell.alive:
                    cell.kill()
                elif live_neighbor_count == 3 and not cell.alive:
                    cell.spawn()
