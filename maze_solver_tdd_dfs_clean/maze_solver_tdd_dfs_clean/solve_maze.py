"""Run this file to solve maze.txt using DFS."""

from loader import load_maze
from renderer import print_maze
from solver import solve_dfs, mark_solution


INPUT_FILE = "maze.txt"


if __name__ == "__main__":
    maze = load_maze(INPUT_FILE)
    path = solve_dfs(maze)
    solved_maze = mark_solution(maze, path)

    print("\nSolved Maze with DFS:\n")
    print_maze(solved_maze)

    if path is None:
        print("\nNo path found.")
    else:
        print(f"\nPath length: {len(path)} cells")
