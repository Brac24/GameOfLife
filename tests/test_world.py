import pytest
from board import board_creator
from cell.cell import Cell
from world.world import World

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

    