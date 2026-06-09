"""Run this file to solve maze.txt using DFS."""

# Import load_maze from loader.py.
# This function reads maze.txt and changes it into a Python maze list.
from loader import load_maze

# Import print_maze from renderer.py.
# This function prints the maze nicely in the terminal.
from renderer import print_maze

# Import solve_dfs and mark_solution from solver.py.
# solve_dfs finds the path using DFS.
# mark_solution puts the solution dots on the maze.
from solver import solve_dfs, mark_solution


# This is the name of the file we want to solve.
# The program will read the maze from maze.txt.
INPUT_FILE = "maze.txt"


# This line means:
# Run the code below only when this file is run directly.
#
# Example:
# python solve_maze.py
#
# If this file is imported by another file,
# the code below will not run automatically.
if __name__ == "__main__":

    # Load the maze from maze.txt.
    # maze will become a list of rows.
    maze = load_maze(INPUT_FILE)

    # Solve the maze using DFS.
    # path will contain the correct path from S to E.
    #
    # If no path is found, path will be None.
    path = solve_dfs(maze)

    # Mark the solution path on the maze.
    # Usually it adds dots or path symbols.
    #
    # If path is None, mark_solution should return the maze unchanged.
    solved_maze = mark_solution(maze, path)

    # Print a title before showing the solved maze.
    print("\nSolved Maze with DFS:\n")

    # Print the solved maze in the terminal.
    print_maze(solved_maze)

    # Check if DFS failed to find a path.
    if path is None:

        # Print this message if there is no solution.
        print("\nNo path found.")

    # If path is not None, DFS found a solution.
    else:

        # Print how many cells are in the solution path.
        # len(path) counts the number of positions in the path.
        print(f"\nPath length: {len(path)} cells")