"""Run this file to generate a maze and save it to maze.txt."""

from generator import generate_maze
from loader import save_maze
from renderer import print_maze


WIDTH = 41
HEIGHT = 21
OUTPUT_FILE = "maze.txt"


if __name__ == "__main__":
    maze = generate_maze(WIDTH, HEIGHT)
    save_maze(maze, OUTPUT_FILE)

    print("\nGenerated Maze:\n")
    print_maze(maze)
    print(f"\nSaved to {OUTPUT_FILE}")
