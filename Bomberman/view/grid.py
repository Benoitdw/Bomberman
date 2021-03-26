from PySide6.QtWidgets import QLabel, QGridLayout, QWidget
from Bomberman.view.cell import Cell


class Grid(QGridLayout):
    def __init__(self):
        super().__init__()
        self.data = None
        self.container = QWidget()
        self.addWidget(QLabel('Bomberman'), 0, 0)

    def update(self, data):
        self.data = data
        self.set_layout()

    def set_layout(self):
        for row in self.data.cells:
            for cell in row:
                self.addWidget(Cell(cell), cell.x, cell.y)