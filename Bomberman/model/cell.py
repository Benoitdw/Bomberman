from typing import Tuple
from Bomberman.utils import HIDDEN, FLAGGED, VISIBLE


class Cell:
    def __init__(self, value: int, position: Tuple, parent):
        self.parent_grid = parent
        self._value = value
        self.x, self.y = position
        self.state = HIDDEN

    def set_visible(self):
        if self.state == HIDDEN:
            if self._value == 100:
                return 0
            else:
                self.state = VISIBLE
            if self._value == 0:
                self._show_neighbors()
        return 1

    def _show_neighbors(self):
        neighbors = self._search_neighbors()
        print(neighbors)
        for neighbor in neighbors:
            print(neighbor.state)
            neighbor.set_visible()
        print('---')

    def _search_neighbors(self):
        neighbors = []
        min_x, min_y, max_x, max_y = self._range_neighbors()
        for row in self.parent_grid.cells[min_y: max_y]:
            for cell in row[min_x:max_x]:
                if cell != self:
                    neighbors.append(cell)
        return neighbors

    def _range_neighbors(self):
        min_y, max_y = max(self.y-1, 0), min(self.y+2, self.parent_grid.shape[0])
        min_x, max_x = max(self.x-1,0), min(self.x+2, self.parent_grid.shape[1])
        return min_x, min_y, max_x, max_y

    def _get_value(self):
        if self._value == 0:
            return ''
        elif self._value == 100:
            return '*'
        else:
            return str(self._value)

    value = property(_get_value)

    def __repr__(self):
        if self.state == HIDDEN:
            return '■'
        if self.state == FLAGGED:
            return '?'
        if self.state == VISIBLE:
            if self._value == 0:
                return ' '
            elif self._value == 100:
                return '*'
            else :
                return str(self._value)
