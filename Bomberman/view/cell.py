from PySide6.QtWidgets import QPushButton
from Bomberman.utils import HIDDEN, FLAGGED, VISIBLE


class Cell(QPushButton):
    def __init__(self, data, parent):
        self.parent = parent
        self.data = data
        super().__init__()
        self.clicked.connect(self.show_value)

    def set_content(self):
        if self.data.state == HIDDEN:
            self.setText('X')
        elif self.data.state == FLAGGED:
            self.setText('?')
        elif self.data.state == VISIBLE:
            self.setText(str(self.data.value))

    def show_value(self):
        if self.data.set_visible() == 1:
            self.parent.update_grid()
        else:
            print('GAME OVER')
