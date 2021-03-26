from PySide6.QtWidgets import QPushButton


class Cell(QPushButton):
    def __init__(self, data):
        self.data = data
        super().__init__(str(data.value))
