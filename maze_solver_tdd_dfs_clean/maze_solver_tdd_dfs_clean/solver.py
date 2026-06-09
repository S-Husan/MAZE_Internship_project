"""DFS maze solver."""

from maze import Maze, START, END, SOLUTION


def solve_dfs(grid):
    """Solve a maze with DFS and return the path.

    The path is a list of (row, col) positions from S to E.
    If no path exists, the function returns None.
    """
    maze = Maze(grid)
    start = maze.find_start()
    end = maze.find_end()

    if start is None:
        raise ValueError("Maze has no start cell marked with S.")

    if end is None:
        raise ValueError("Maze has no end cell marked with E.")

    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            return path

        row, col = current

        for neighbor in reversed(maze.get_neighbors(row, col)):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


def mark_solution(grid, path):
    """Return a copy of the maze with the DFS solution marked by '*'."""
    maze_copy = [row[:] for row in grid]

    if path is None:
        return maze_copy

    for row, col in path:
        if maze_copy[row][col] not in (START, END):
            maze_copy[row][col] = SOLUTION

    return maze_copy
