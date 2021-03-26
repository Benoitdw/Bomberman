from PySide6.QtGui import QAction
from Bomberman.bomberman import Game


class NewGame(QAction):
    def __init__(self, parent, root):
        super().__init__('New Game', parent)
        self.root = root
        self.setStatusTip("Make a new game?")
        self.triggered.connect(self._make_new_game)

    def _make_new_game(self):
        new_game = Game(self.root.shape_grid)
        new_game.start()
        self.root.set_data(new_game)
