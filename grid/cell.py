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
        min_x, min_y, max_x, max_y = self._range_neighbors()
        for cell in self.parent_grid.cells[min_y: max_y, min_x:max_x]:
            if cell != self:
                neighbors.append(cell)
        return neighbors

    def _range_neighbors(self):
        min_y, max_y = max(self.y-1, 0), min(self.y+2, self.parent_grid.shape[0])
        min_x, max_x = max(self.x-1,0), min(self.x+2, self.parent_grid.shape[1])
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
