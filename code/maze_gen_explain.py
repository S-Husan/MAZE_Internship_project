"""
DFS maze generator.

This file creates a maze.
It uses DFS style recursive backtracking.
That means the program goes deep in one direction,
then comes back when it cannot continue.
"""

# random is used to make the maze different each time.
import random

# deque is used like a queue.
# Here it is used to calculate distances from the start.
from collections import deque

# We import symbols from maze.py.
# WALL means wall cell.
# OPEN means walkable cell.
# START means starting point.
# END means ending point.
from maze import WALL, OPEN, START, END


# This function checks if the maze size is valid.
def _validate_size(width, height):

    # If width or height is smaller than 5, the maze is too small.
    if width < 5 or height < 5:
        raise ValueError("Maze width and height must both be at least 5.")

    # The maze size must be odd.
    # Example: 41 and 21 are good.
    # Even numbers do not work well with this DFS maze algorithm.
    if width % 2 == 0 or height % 2 == 0:
        raise ValueError("Maze width and height must be odd numbers, for example 41 and 21.")


# This function creates and returns a new maze.
def generate_maze(width=41, height=21, seed=None):
    """
    Generate and return a new DFS maze.

    width: how many columns the maze has.
    height: how many rows the maze has.
    seed: optional number used to make the same maze again in tests.

    The function returns a 2D list.
    Example:
    [
        ['#', '#', '#'],
        ['S', '.', 'E'],
        ['#', '#', '#']
    ]
    """

    # First, check if width and height are correct.
    _validate_size(width, height)

    # Create a random generator.
    # If seed is given, the maze will be repeatable.
    # This is useful for testing.
    rng = random.Random(seed)

    # Create a maze full of walls.
    # It creates "height" rows.
    # Each row has "width" cells.
    maze = [[WALL for _ in range(width)] for _ in range(height)]

    # This inner function carves paths in the maze.
    # row means vertical position.
    # col means horizontal position.
    def carve(row, col):

        # Make the current cell open.
        # This means we can walk here.
        maze[row][col] = OPEN

        # These are possible moves.
        # We move by 2 cells because there is a wall between cells.
        #
        # (-2, 0) means move up.
        # (2, 0) means move down.
        # (0, -2) means move left.
        # (0, 2) means move right.
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        # Shuffle directions randomly.
        # This makes every maze look different.
        rng.shuffle(directions)

        # Try every direction.
        for dr, dc in directions:

            # Calculate the new row.
            new_row = row + dr

            # Calculate the new column.
            new_col = col + dc

            # Check three things:
            #
            # 1. new_row is inside the maze.
            # 2. new_col is inside the maze.
            # 3. the new cell is still a wall.
            #
            # If the new cell is a wall, it means it was not visited yet.
            if (
                1 <= new_row < height - 1
                and 1 <= new_col < width - 1
                and maze[new_row][new_col] == WALL
            ):

                # Remove the wall between current cell and new cell.
                #
                # Example:
                # If we move 2 cells right,
                # dc // 2 gives 1,
                # so it opens the wall in the middle.
                maze[row + dr // 2][col + dc // 2] = OPEN

                # Open the new cell.
                maze[new_row][new_col] = OPEN

                # Continue carving from the new cell.
                # This is recursion.
                carve(new_row, new_col)

    # This is the first inside position of the maze.
    # We start carving from row 1, column 1.
    start_inside = (1, 1)

    # Start DFS maze generation.
    carve(*start_inside)

    # This is the visible start position.
    # It is on the border of the maze.
    start = (1, 0)

    # Put START symbol in the maze.
    # start[0] is row.
    # start[1] is column.
    maze[start[0]][start[1]] = START

    # Choose an exit far away from the start.
    exit_position = _choose_far_exit(maze, start_inside, rng)

    # Put END symbol in the maze.
    maze[exit_position[0]][exit_position[1]] = END

    # Return the final maze.
    return maze


# This function chooses an exit far from the start.
def _choose_far_exit(maze, start_inside, rng):
    """
    Choose a border exit far away from the start.

    The exit will be placed on the edge of the maze.
    The function tries to choose a far place,
    so the maze is more interesting.
    """

    # Get maze height.
    height = len(maze)

    # Get maze width.
    width = len(maze[0])

    # Get distances from the starting inside cell.
    # This tells how far every open cell is from the start.
    distances = _distances_from(maze, start_inside)

    # candidates will store possible exit positions.
    candidates = []

    # Check right border exits.
    for row in range(1, height - 1):

        # If the cell near the right border is open,
        # we can put an exit on the border next to it.
        if maze[row][width - 2] == OPEN:

            # Add possible exit position and its distance.
            candidates.append(((row, width - 1), distances.get((row, width - 2), -1)))

    # Check bottom border exits.
    for col in range(1, width - 1):

        # If the cell near the bottom border is open,
        # we can put an exit on the bottom border.
        if maze[height - 2][col] == OPEN:

            # Add possible exit position and its distance.
            candidates.append(((height - 1, col), distances.get((height - 2, col), -1)))

    # Check top-right side exit.
    if maze[1][width - 2] == OPEN:

        # Add this possible exit.
        candidates.append(((1, width - 1), distances.get((1, width - 2), -1)))

    # Check bottom-left side exit.
    if maze[height - 2][1] == OPEN:

        # Add this possible exit.
        candidates.append(((height - 1, 1), distances.get((height - 2, 1), -1)))

    # Find the biggest distance.
    # This means the farthest possible exit.
    best_distance = max(distance for _, distance in candidates)

    # Get all exits that have the best distance.
    # Sometimes more than one exit can be equally far.
    farthest = [position for position, distance in candidates if distance == best_distance]

    # Randomly choose one of the farthest exits.
    return rng.choice(farthest)


# This function calculates distances from the start cell.
def _distances_from(maze, start):
    """
    Return shortest distances from one open cell to all open cells.

    Important:
    This part uses a queue to measure distance.
    It is not the maze solver.
    It is only used to choose a far exit.
    """

    # Create a queue and put the start cell inside it.
    queue = deque([start])

    # Store distance for the start cell.
    # Distance from start to start is 0.
    distances = {start: 0}

    # These are four normal moves.
    #
    # (-1, 0) means up.
    # (0, 1) means right.
    # (1, 0) means down.
    # (0, -1) means left.
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Continue while the queue is not empty.
    while queue:

        # Take the first cell from the queue.
        row, col = queue.popleft()

        # Try all four directions.
        for dr, dc in directions:

            # Calculate next row.
            new_row = row + dr

            # Calculate next column.
            new_col = col + dc

            # Check if the new cell:
            #
            # 1. is inside the maze,
            # 2. is open,
            # 3. was not visited before.
            if (
                0 <= new_row < len(maze)
                and 0 <= new_col < len(maze[0])
                and maze[new_row][new_col] == OPEN
                and (new_row, new_col) not in distances
            ):

                # Save distance to this new cell.
                # It is one step more than the current cell.
                distances[(new_row, new_col)] = distances[(row, col)] + 1

                # Add this new cell to the queue.
                # Later we will check its neighbors too.
                queue.append((new_row, new_col))

    # Return all calculated distances.
    return distances