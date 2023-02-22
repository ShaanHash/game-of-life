import sys
from renderenginer import render
from boardstate import random_state
from transformationengine import next_state
import os
import time
import cursor

if __name__ == "__main__":

    # Define simulation variables
    height = 50
    width = 100
    generations = 100

    # Hide the blinking cursor
    cursor.hide()

    # Intiate a random board_state
    board_state = random_state(height, width,15)

    print("Simulation Starting...")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Iterate through each generation
    for i in range(0,generations):

        # Render
        # Wait
        # Transform
        # Clear

        render(board_state)
        time.sleep(0.20)
        board_state = next_state(board_state)
        if i != generations -1:
            os.system('cls' if os.name == 'nt' else 'clear')

    # Return the blinking cursor
    cursor.show()