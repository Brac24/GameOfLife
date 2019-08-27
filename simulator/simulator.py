from board import board_creator

class Simulator():
    def __init__(self, x, y):
        self.board = board_creator.randomstate(x,y)

    def get_board_size(self):
        return [len(self.board), len(self.board[0])]
        