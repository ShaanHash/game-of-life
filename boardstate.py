import numpy as np
import random

height = 10
width = 10


def dead_state(height: int, width: int) -> np.ndarray:
    """
    Create a boardstate with only 0s

    :param int height: The height of the board
    :param int width: The width of the board
    :return: A Numpy 2-dimensional array
    :rtype: np.ndarray
    """

    return np.zeros((height,width),object)


def random_state(height: int, width: int, threshold: int):
    """
    Create a random boardstate with a specified threshold of 1s

    :param int height: The height of the board
    :param int width: The width of the board
    :param int threshold: An int from 1-100 that represents the average number of 1s
    :return: A Numpy 2-dimensional array
    :rtype: np.ndarray
    """

    intial_board = dead_state(height, width)

    for i in range(len(intial_board)):
        for j in range(len(intial_board[i])):
            random_number = random.randint(0,100)

            if random_number <= threshold:
                intial_board[i][j] = 1
            else:
                intial_board[i][j] = 0

    return intial_board





