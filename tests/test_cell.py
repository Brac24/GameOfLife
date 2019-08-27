import pytest
from cell.cell import Cell

def test_cell_init_correct_location_not_alive():
    location = [1,2]
    cell = Cell(location, True)
    assert cell.location == [1,2]
    assert cell.alive == True

def test_cell_correct_location_alive():
    location = [3,7]
    cell = Cell(location, False)
    assert cell.location == [3,7]
    assert cell.alive == False

def test_cell_kill_dead_state():
    location = [1,2]
    cell = Cell(location, True)

    cell.kill()
    assert cell.alive is False
    assert cell.location is location

def test_cell_spawn_alive_state():
    location = [1,2]
    cell = Cell(location, False)
    cell.spawn()
    assert cell.alive is True
    assert cell.location is location

def test_cell_neighbor_locations_correct(): 
    #There are a max of 8 neighbors for any one cell on a grid
    location = [2,3]
    cell = Cell(location, True)
    row_above = location[0] -1 # take x location and subtract by one to get row above cell
    row_below = location[0] + 1 # increment x location to get row below cell
    col_left = location[1] - 1 # decrement column value to get column to the left of the cell
    col_right = location[1] + 1 # column to the right of the cell

    neighbors_row_above = helper_get_above_neigbors(location)
    neighbors_row_on = helper_get_on_neighbors(location)
    neighbors_row_below = helper_get_below_neigbors(location)
    neighbors_expected = neighbors_row_above
    neighbors_expected.extend(neighbors_row_on)
    neighbors_expected.extend(neighbors_row_below)
    neighbor_locations = cell.get_neighbors()

    assert neighbors_expected == neighbor_locations

def helper_get_below_neigbors(location):
    row_below = location[0] + 1 # increment x location to get row below cell
    col_left = location[1] - 1 # decrement column value to get column to the left of the cell
    col_right = location[1] + 1 # column to the right of the cell
    neighbors_row_below = [[row_below,col_left], [row_below, location[1]], [row_below, col_right]]
    return neighbors_row_below

def helper_get_above_neigbors(location):
    row_above = location[0] -1 # take x location and subtract by one to get row above cell
    col_left = location[1] - 1 # decrement column value to get column to the left of the cell
    col_right = location[1] + 1 # column to the right of the cell
    neighbors_row_above = [[row_above,col_left], [row_above, location[1]], [row_above, col_right]]
    return neighbors_row_above

def helper_get_on_neighbors(location):
    col_left = location[1] - 1 # decrement column value to get column to the left of the cell
    col_right = location[1] + 1 # column to the right of the cell
    neighbors_row_on = [[location[0],col_left], [location[0], col_right]]
    return neighbors_row_on


def test_cell_init_at_origin_no_above_and_below_neighbors():
    location = [0,0]
    cell = Cell(location, True)
    neighbors_expected = [[0,1],[1,1],[1,0]]

    neighbors = cell.get_neighbors()
    assert neighbors == neighbors_expected