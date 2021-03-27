from Bomberman.model.grid import Grid
from typing import Tuple


class Bomberman:
    def __init__(self):
        self.shape = (10, 10)

    def execution(self):
        restart = True
        while restart:
            grid = Grid(self.shape)
            current_game = Game(grid)
            current_game.start()
            is_game_over = False
            while not is_game_over:
                print(current_game.grid.cells)
                action_value = current_game.choose()
                is_game_over = current_game.is_game_over(action_value)
            restart = int(input("Do you cant to stop? (type 0 to stop)"))


class Game:
    def __init__(self, grid_shape: Tuple):
        self.grid = Grid(grid_shape)

    def choose(self):  # CLI
        coords_x = int(input("coordonnées x?"))
        coords_y = int(input('coordonnées y?'))
        actions = {1: self.grid.cells[coords_y][coords_x].set_visible}
        action = 1
        val = actions[action]()
        return val

    def start(self):
        self.grid.generate(self)

    @staticmethod
    def is_game_over(return_action_value):  # CLI

        if return_action_value == 0:
            print('YOU LOST!')
            return True
        else:
            return False
