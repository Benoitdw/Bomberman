from PySide6.QtWidgets import QPushButton
from src.utils import HIDDEN, FLAGGED, VISIBLE


class Cell(QPushButton):
    def __init__(self, data, parent):
        self.parent = parent
        self.data = data
        super().__init__()
        self.clicked.connect(self.show_value)
        self.setMaximumSize(20,20)

    def set_content(self):
        if self.data.state == HIDDEN:
            self.setText('X')
        elif self.data.state == FLAGGED:
            self.setText('?')
        elif self.data.state == VISIBLE:
            self.setText(str(self.data.value))
            self.setDown(True)
            self.setCheckable(False)

    def show_value(self):
        if self.data.set_visible() == 1:
            self.parent.update_grid()
        else: # to debug
            print('GAME OVER')
