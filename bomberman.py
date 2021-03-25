from grid import Grid


class Bomberman:
    def __init__(self):
        self.grid = Grid((8,8))

    def execution(self):
        while True:
            current_game = Game(self.grid)
            current_game.start()
            while True:
                current_game.choose()
                print(current_game.grid.cells)


class Game:
    def __init__(self, grid):
        self.grid = grid

    def choose(self): # TODO : remove when gui
        coords_x = int(input("coordonnées x?"))
        coords_y = int(input('coordonnées y?'))
        if self.grid.cells[coords_y][coords_x].set_visible() == 0:# TODO : Define action
            self.game_over()

    def start(self):
        self.grid.generate(self)
        print(self.grid.cells)

    def game_over(self):
        print('YOU LOST!')