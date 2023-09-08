from src.view.main_window import MainWindow
from PySide6.QtWidgets import QApplication

game = QApplication()
main_window = MainWindow()
main_window.show()
game.exec_()