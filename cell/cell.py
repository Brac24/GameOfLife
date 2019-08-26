class Cell:

    def __init__(self, location, alive):
            self.location = location
            self.alive = alive

            #neighbors
            #test [0,0] edge 
            row_above = location[0] - 1
            row_below = location[0] + 1
            col_left = location[1] - 1
            col_right = location[1] + 1

            left_top_corner = [row_above, col_left]
            above = [row_above, location[1]]
            right_top_corner = [row_above, col_right]
            left = [location[0], col_left]
            right = [location[0], col_right]
            bottom_left_corner = [row_below, col_left]
            below = [row_below, location[1]]
            bottom_right_corner = [row_below, col_right]

            self.neighbors = [left_top_corner, above, right_top_corner, left, right, bottom_left_corner, below, bottom_right_corner]

    def kill(self):
        self.alive = False

    def spawn(self):
        self.alive = True

    def get_neighbors(self):
        return self.neighbors
