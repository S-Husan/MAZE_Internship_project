"""Simple command-line menu for the DFS maze project."""

from generator import generate_maze
from loader import save_maze, load_maze
from renderer import print_maze
from solver import solve_dfs, mark_solution


if __name__ == "__main__":
    print("1. Generate maze")
    print("2. Solve maze.txt with DFS")
    choice = input("Choose: ")

    if choice == "1":
        maze = generate_maze(41, 21)
        save_maze(maze, "maze.txt")
        print("\nGenerated Maze:\n")
        print_maze(maze)

    elif choice == "2":
        maze = load_maze("maze.txt")
        path = solve_dfs(maze)
        solved_maze = mark_solution(maze, path)
        print("\nSolved Maze with DFS:\n")
        print_maze(solved_maze)

    else:
        print("Invalid choice.")
