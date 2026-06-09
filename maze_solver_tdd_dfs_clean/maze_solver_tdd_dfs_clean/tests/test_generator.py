import unittest

from generator import generate_maze
from maze import Maze
from solver import solve_dfs


class TestGenerator(unittest.TestCase):
    def test_generator_creates_correct_size(self):
        maze = generate_maze(11, 7, seed=1)

        self.assertEqual(len(maze), 7)
        self.assertEqual(len(maze[0]), 11)

    def test_generator_creates_start_and_end(self):
        maze = generate_maze(11, 7, seed=2)
        maze_obj = Maze(maze)

        self.assertIsNotNone(maze_obj.find_start())
        self.assertIsNotNone(maze_obj.find_end())

    def test_generated_maze_is_solvable_by_dfs(self):
        maze = generate_maze(21, 11, seed=3)
        path = solve_dfs(maze)

        self.assertIsNotNone(path)
        self.assertGreater(len(path), 1)

    def test_generator_rejects_even_size(self):
        with self.assertRaises(ValueError):
            generate_maze(10, 10)


if __name__ == "__main__":
    unittest.main()
