from PySide6.QtWidgets import QLabel, QGridLayout, QWidget
from src.view.cell import Cell


class Grid(QGridLayout):
    def __init__(self):
        super().__init__()
        self.data = None
        self.cells = []
        self.container = QWidget()
        self.filler = QLabel('Bomberman')
        self.addWidget(self.filler, 0, 0)
        self.setHorizontalSpacing(0)
        self.setVerticalSpacing(0)

    def update(self, data):
        self.data = data
        self.set_layout()
        self.filler.setText('')  # TODO: find a proper way to delete this shit

    def set_layout(self):
        for cell in self._iterate_grid_data():
            widget = Cell(cell, self)
            self.cells.append(widget)
            self.addWidget(widget, cell.x, cell.y)
        self.update_grid()

    def update_grid(self):
        for cell in self._iterate_grid_cells():
            cell.set_content()

    def _iterate_grid_data(self):
        for row in self.data.cells:
            for cell in row:
                yield cell

    def _iterate_grid_cells(self):
        for cell in self.cells:
            yield cell