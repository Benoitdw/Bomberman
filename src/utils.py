import numpy as np


Array = np.ndarray



HIDDEN = 0
VISIBLE = 1
FLAGGED = 2

kernel_3x3 = np.ones((3, 3), dtype=bool)
kernel_3x3[1, 1] = False