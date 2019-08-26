import pytest
from board import board_creator

def test_proper_boardsize():
    expectedRows = 4
    expectedCols = 3
    board = board_creator.deadstate(expectedRows, expectedCols)
    rows = len(board)
    cols = len(board[0])
    assert rows == expectedRows
    assert cols == expectedCols

def test_no_live_cells():
    board = board_creator.deadstate(6,8)
    assert 1 not in board

def test_all_dead_cells():
    expected = [[0,0], [0,0]]
    board = board_creator.deadstate(2,2)
    assert board == expected