import numpy as np

"""
The cell then updates its own liveness according to 4 rules:

    Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

"""


def next_state(board_state: np.ndarray) -> np.ndarray :
    
    return np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ],object)