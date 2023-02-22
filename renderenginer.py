from boardstate import random_state
import numpy as np
from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

# Use a regex-highlighter class to highlight the correct symbols
class GridHighlighter(RegexHighlighter):

    base_style = "cell."
    highlights = [r"(?P<alive>[$])", r"(?P<dead>['])"]


# Render the board to the console using symbols
def render(board_state: np.ndarray) -> None:

    # create a new array of the same shape
    render_array = np.zeros(board_state.shape, object)

    # Replace each 1 with a symbol and each 0 with a symbol ...
    # ... leaving the original board_state untouched
    for i in range(len(board_state)):
        for j in range(len(board_state[i])):
            if board_state[i][j] == 1:
                render_array[i][j] = "$"
            else:
                render_array[i][j] = "'"


    theme = Theme({"cell.alive": "bold green", "cell.dead": "black" })
    console = Console(highlighter=GridHighlighter(), theme=theme)

    for i in render_array: 
        console.print(*i, sep=" ")

    return None

