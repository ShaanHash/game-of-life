from renderenginer import render
from transformationengine import next_state
from boardstate import random_state
import numpy as np

"""
The cell then updates its own liveness according to 4 rules:

    Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

"""

def test_1():

    intial_state = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ],object)
    expected_state = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ],object)

    new_state = next_state(intial_state)

    if ((new_state == expected_state).all()):
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
        print("Initial State:")
        render(intial_state)
        print("Next State:")
        render(new_state)
        print("Expected State")
        render(expected_state)

def test_2():

    intial_state = np.array([
        [1,0,0],
        [1,1,0],
        [0,0,0],
        ],object)
    expected_state = np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1],
        ],object)

    new_state = next_state(intial_state)

    if (np.array_equal(new_state, expected_state)):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")
        print("Initial State:")
        render(intial_state)
        print("Next State:")
        render(new_state)
        print("Expected State")
        render(expected_state)  

def test_3():

    intial_state = random_state(10,10,75)
    expected_state = np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1],
        ],object)

    new_state = next_state(intial_state)

    if (np.array_equal(new_state, expected_state)):
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")
        print("Initial State:")
        render(intial_state)
        print("Next State:")
        render(new_state)
        print("Expected State")
        render(expected_state) 



test_1()
test_2()

