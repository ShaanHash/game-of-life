import numpy as np


"""
The cell then updates its own liveness according to 4 rules:

    Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

"""


def next_state(board_state: np.ndarray) -> np.ndarray :

    # Create an empty board of the same shape
    transformed_board_state = np.zeros(board_state.shape,object)
    
    # We need to know when to wrap overflow positive indices ...
    # ... back to 0
    (max_row_index, max_col_index) = board_state.shape
    max_row_index -= 1
    max_col_index -= 1

    # Loop through each cell
    for row in range(len(board_state)):
        for col in range(len(board_state[row])):

            origin_cell = board_state[row][col]

            # Control the indices
            # Negative indices will wrap around the array
            # However, overflow indices (greater than the size of the array)...
            # ... will need to wrap to the start of the array
            north_row = row - 1
            south_row = 0 if row == max_row_index else row + 1
            west_col = col - 1
            east_col = 0 if col == max_col_index else col + 1 

            # Use the controled indices to determine the neighburs of the current cell
            north_cell = board_state[north_row][col]
            south_cell = board_state[south_row][col]
            
            west_cell = board_state[row][west_col]
            east_cell = board_state[row][east_col]

            north_west_cell = board_state[north_row][west_col]
            north_east_cell = board_state[north_row][east_col]
            south_west_cell = board_state[south_row][west_col]
            south_east_cell = board_state[south_row][east_col]

            # Find out how many alive neighburs the cell has
            total_adjacent = (
                north_cell +
                south_cell +
                west_cell +
                east_cell +
                north_west_cell +
                north_east_cell +
                south_west_cell + 
                south_east_cell
            )

            # Transform it based on the rule-set
            if origin_cell == 0:
                transformed_board_state[row][col] = 1 if total_adjacent == 3 else 0
            elif origin_cell == 1:
                match total_adjacent:
                    case 0:
                        transformed_board_state[row][col] = 0
                    case 1:
                        transformed_board_state[row][col] = 0
                    case 2:
                        transformed_board_state[row][col] = 1
                    case 3:
                        transformed_board_state[row][col] = 1
                    case _:
                        transformed_board_state[row][col] = 0

    return transformed_board_state