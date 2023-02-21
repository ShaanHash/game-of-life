import sys
from renderenginer import render
from boardstate import random_state

if __name__ == "__main__":

    height = 3
    width = 3

    board_state = random_state(height, width,30)

    render(board_state)

    sys.exit(0)
