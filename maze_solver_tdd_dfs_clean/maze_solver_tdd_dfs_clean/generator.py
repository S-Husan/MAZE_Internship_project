"""DFS maze generator.

The generator creates a solvable maze using recursive backtracking,
which is a depth-first search style algorithm.
"""

import random
from collections import deque

from maze import WALL, OPEN, START, END


def _validate_size(width, height):
    if width < 5 or height < 5:
        raise ValueError("Maze width and height must both be at least 5.")

    if width % 2 == 0 or height % 2 == 0:
        raise ValueError("Maze width and height must be odd numbers, for example 41 and 21.")


def generate_maze(width=41, height=21, seed=None):
    """Generate and return a new DFS maze.

    Args:
        width: Number of columns in the maze.
        height: Number of rows in the maze.
        seed: Optional random seed. Use it in tests to make the maze repeatable.

    Returns:
        A list of lists containing '#', '.', 'S', and 'E'.
    """
    _validate_size(width, height)

    rng = random.Random(seed)
    maze = [[WALL for _ in range(width)] for _ in range(height)]

    def carve(row, col):
        maze[row][col] = OPEN

        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        rng.shuffle(directions)

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                1 <= new_row < height - 1
                and 1 <= new_col < width - 1
                and maze[new_row][new_col] == WALL
            ):
                maze[row + dr // 2][col + dc // 2] = OPEN
                maze[new_row][new_col] = OPEN
                carve(new_row, new_col)

    start_inside = (1, 1)
    carve(*start_inside)

    start = (1, 0)
    maze[start[0]][start[1]] = START

    exit_position = _choose_far_exit(maze, start_inside, rng)
    maze[exit_position[0]][exit_position[1]] = END

    return maze


def _choose_far_exit(maze, start_inside, rng):
    """Choose a border exit far away from the start."""
    height = len(maze)
    width = len(maze[0])

    distances = _distances_from(maze, start_inside)
    candidates = []

    for row in range(1, height - 1):
        if maze[row][width - 2] == OPEN:
            candidates.append(((row, width - 1), distances.get((row, width - 2), -1)))

    for col in range(1, width - 1):
        if maze[height - 2][col] == OPEN:
            candidates.append(((height - 1, col), distances.get((height - 2, col), -1)))

    if maze[1][width - 2] == OPEN:
        candidates.append(((1, width - 1), distances.get((1, width - 2), -1)))

    if maze[height - 2][1] == OPEN:
        candidates.append(((height - 1, 1), distances.get((height - 2, 1), -1)))

    best_distance = max(distance for _, distance in candidates)
    farthest = [position for position, distance in candidates if distance == best_distance]

    return rng.choice(farthest)


def _distances_from(maze, start):
    """Return shortest grid distances from one open cell to all open cells."""
    queue = deque([start])
    distances = {start: 0}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < len(maze)
                and 0 <= new_col < len(maze[0])
                and maze[new_row][new_col] == OPEN
                and (new_row, new_col) not in distances
            ):
                distances[(new_row, new_col)] = distances[(row, col)] + 1
                queue.append((new_row, new_col))

    return distances
