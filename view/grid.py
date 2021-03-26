from PySide6.QtWidgets import QLabel


class Grid(QLabel):
    def __init__(self):
        super().__init__()
        self.setText('Yo les Potos')
        self.data = None

    def update(self, data):
        self.data = data
        self.setText('')
        self.setText(str(data))