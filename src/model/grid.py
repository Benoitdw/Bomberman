import numpy as np
from src.model.cell import Cell
from typing import Tuple
from scipy import signal
from src.utils import Array, kernel_3x3


class Grid:
    def __init__(self,
                 shape: Tuple[int, int],
                 kernel=kernel_3x3):
        self.parent_game = None
        self.shape = shape
        self.kernel = kernel
        self.cells = []

        self._neighbors = None
        self._matrix = np.zeros(self.shape, dtype=bool)
        self._state = np.zeros(self.shape, dtype=bool)

    def generate(self, parent) -> None:
        self.parent_game = parent
        self._randomize()
        self._neighbors = self._count_neighbors()
        mask = np.ma.array(self._neighbors, mask=self._bombs_location, fill_value=None)
        self._matrix = mask.filled(fill_value=100)
        self._make_cells()

    def _make_cells(self) -> None:
        for y, row in enumerate(self._matrix):
            cells = []
            for x, cell in enumerate(row):
                cells.append(Cell(cell, (x, y), self))
            self.cells.append(cells)
        self.cells = np.array(self.cells)

    def _randomize(self, density: float = 0.1) -> None:
        self._bombs_location = np.random.random(self.shape) < density

    def _count_neighbors(self) -> Array:
        return signal.convolve2d(self._bombs_location.astype('u1'), self.kernel, mode='same')

    def __str__(self) -> str:
        return '\n'.join(
            ''.join('*' if cell == 100 else str(cell) if cell >= 1 else ' ' for cell in line_m) for line_m, line_s in
            zip(self._matrix, self._state))


if __name__ == '__main__':
    grid = Grid((2, 2))
    grid.generate()
    grid.init_cell()
    print(grid)
