from boardstate import random_state
import numpy as np
from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

class GridHighlighter(RegexHighlighter):

    base_style = "cell."
    highlights = [r"(?P<alive>[$])", r"(?P<dead>['])"]


def render(board_state: np.ndarray) -> None:

    for i in range(len(board_state)):
        for j in range(len(board_state[i])):
            if board_state[i][j] == 1:
                board_state[i][j] = "$"
            else:
                board_state[i][j] = "'"


    theme = Theme({"cell.alive": "bold green", "cell.dead": "black" })
    console = Console(highlighter=GridHighlighter(), theme=theme)

    for i in board_state: 
        console.print(*i, sep=" ")


