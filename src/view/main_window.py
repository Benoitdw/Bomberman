from PySide6.QtWidgets import QMainWindow, QWidget
from src.controler.menu_action import NewGame
from src.view.grid import Grid


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bomberman')
        self.data = None
        self.shape_grid = (5,5)
        self.grid = Grid()

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(NewGame(self, self))
        test = QWidget()
        test.setLayout(self.grid)
        self.setCentralWidget(test)

    def set_data(self, data):
        self.data = data
        self.grid.update(data.grid)
