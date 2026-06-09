"""Maze model and small helper methods.

Coordinate rule used in this project:
    position = (row, col)
    grid[row][col]
"""

WALL = "#"
OPEN = "."
START = "S"
END = "E"
SOLUTION = "*"


class Maze:
    """A simple wrapper around a 2D maze grid."""

    def __init__(self, grid):
        if not grid:
            raise ValueError("Maze grid cannot be empty.")

        width = len(grid[0])
        if width == 0:
            raise ValueError("Maze rows cannot be empty.")

        for row in grid:
            if len(row) != width:
                raise ValueError("Maze must be rectangular. All rows need the same length.")

        self.grid = grid
        self.rows = len(grid)
        self.cols = width

    def find_symbol(self, symbol):
        """Return the first position of a symbol, or None if it does not exist."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == symbol:
                    return (row, col)
        return None

    def find_start(self):
        """Find the start cell marked with S."""
        return self.find_symbol(START)

    def find_end(self):
        """Find the end cell marked with E."""
        return self.find_symbol(END)

    def in_bounds(self, row, col):
        """Return True if a position is inside the grid."""
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_wall(self, row, col):
        """Return True if a position is a wall."""
        return self.grid[row][col] == WALL

    def is_walkable(self, row, col):
        """Return True if DFS can move onto this cell."""
        return self.in_bounds(row, col) and not self.is_wall(row, col)

    def get_neighbors(self, row, col):
        """Return walkable neighboring cells in up, right, down, left order."""
        neighbors = []
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if self.is_walkable(new_row, new_col):
                neighbors.append((new_row, new_col))

        return neighbors

    def copy_grid(self):
        """Return a deep copy of the grid."""
        return [row[:] for row in self.grid]
