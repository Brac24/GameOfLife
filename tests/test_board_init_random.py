import pytest
from board import board_creator

#Some of these tests will fail from time to time because we are dealing with randomness
#It is bad practice to test with randomness but these are mainly to see how good my random board generation is

def test_consecutive_boards_not_equal():
    board1 = board_creator.randomstate(20,20)
    board2 = board_creator.randomstate(20,20)

    assert board1 != board2

def test_rows_not_equal():
    board = board_creator.randomstate(20,20)

    assert board[0] != board[1]

def test_multiple_random_boards_not_equal():
    boards = []
    for i in range(3):
        boards.append(board_creator.randomstate(15,15))
    
    assert boards[0] not in boards[1]
    assert boards[0] not in boards[2]