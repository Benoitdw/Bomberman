from typing import Tuple
from utils import HIDDEN, FLAGGED, VISIBLE


class Cell:
    def __init__(self, value: int, position: Tuple, parent):
        self.parent_grid = parent
        self.value = value
        self.x, self.y = position
        self.state = HIDDEN

    def set_visible(self):
        if self.state == HIDDEN:
            if self.value == 100:
                return 0
            else:
                self.state = VISIBLE
            if self.value == 0:
                self._show_neighbors()
        return 1

    def _show_neighbors(self):
        neighbors = self._search_neighbors()
        for neighbor in neighbors:
            neighbor.set_visible()

    def _search_neighbors(self):
        neighbors = []
        min_x, min_y, max_x, max_y = self._range_neighbors() # Gère les cellules en bord de grille
        for row in self.parent_grid.cells[min_y: max_y]:
            for cell in row[min_x: max_x]:
                if cell != self:
                    neighbors.append(cell)
        return neighbors

    def _range_neighbors(self):
        min_y, max_y = self.y-1, self.y+2
        if self.y == 0:
            min_y = 0
        elif self.y == self.parent_grid.shape[0]:
            max_y = self.y
        min_x, max_x = self.x-1, self.x+2
        if self.x == 0:
            min_x =0
        elif self.x == self.parent_grid.shape[1]:
            max_x = self.x
        return min_x, min_y, max_x, max_y

    def __repr__(self):
        if self.state == HIDDEN:
            return '■'
        if self.state == FLAGGED:
            return '?'
        if self.state == VISIBLE:
            if self.value == 0:
                return ' '
            elif self.value == 100:
                return '*'
            else :
                return str(self.value)
