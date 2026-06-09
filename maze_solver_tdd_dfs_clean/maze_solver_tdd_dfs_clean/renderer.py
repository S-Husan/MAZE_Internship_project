"""Terminal rendering helpers."""

PRETTY_SYMBOLS = {
    "#": "█",
    ".": " ",
    "*": "●",
    "S": "S",
    "E": "E",
}


def maze_to_string(maze, pretty=True):
    lines = []

    for row in maze:
        if pretty:
            lines.append("".join(PRETTY_SYMBOLS.get(cell, cell) for cell in row))
        else:
            lines.append("".join(row))

    return "\n".join(lines)


def print_maze(maze, pretty=True):
    print(maze_to_string(maze, pretty=pretty))
