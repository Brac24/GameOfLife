import pytest
from board import board_creator
from cell.cell import Cell
from world.world import World

def get_test_board():
    rows = []
    rows.append([1,0,1,1])
    rows.append([0,0,1,0])
    board = []
    board.append(rows[0])
    board.append(rows[1])
    return board

def get_test_board_over_population():
    rows = []
    rows.append([1,1,1,1])
    rows.append([1,1,1,0])
    board = []
    board.append(rows[0])
    board.append(rows[1])
    return board

def test_world_init_cell_in_correct_state():
    dead_board = board_creator.deadstate(5,5)
    world = World(dead_board)
    cell = world.cell_at(2,2)
    assert cell.alive == False

def test_world_init_cell_in_correct_state2():
    rows = []
    rows.append([1,0,0,1])
    rows.append([0,0,1,1])
    board = []
    board.append(rows[0])
    board.append(rows[1])
    world = World(board)
    cell = world.cell_at(1,2)
    assert cell.alive == True

def test_world_cell_dies_off():
    board = get_test_board()
    world = World(board)
    world.next_day()
    cell = world.cell_at(0,0)
    assert cell.alive == False

def test_world_cell_spawns():
    board = get_test_board()
    world = World(board)
    world.next_day()
    cell = world.cell_at(1, 3)
    assert cell.alive == True

def test_world_cell_dies_over_population():
    board = get_test_board_over_population()
    world = World(board)
    world.next_day()
    cell = world.cell_at(0,1)
    assert cell.alive == False



    