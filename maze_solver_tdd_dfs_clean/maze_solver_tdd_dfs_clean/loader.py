"""Load and save maze text files."""


def load_maze(filename="maze.txt"):
    with open(filename, "r", encoding="utf8") as file:
        return [list(line.rstrip("\n")) for line in file if line.rstrip("\n")]


def save_maze(maze, filename="maze.txt"):
    with open(filename, "w", encoding="utf8") as file:
        for row in maze:
            file.write("".join(row) + "\n")
