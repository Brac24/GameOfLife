from board import board_creator
from world.world import World
import os
import time

class Simulator():
    def __init__(self, x, y):
        self.board = board_creator.randomstate(x,y)

    def get_board_size(self):
        return [len(self.board), len(self.board[0])]

    if __name__ == '__main__':
        board = board_creator.randomstate(60,205)
        world = World(board)
        while True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            board_creator.render_world(world.world)
            world.next_day()
            print('-----------------------------------------------------------------------------------------------------')
            #time.sleep(.05)



