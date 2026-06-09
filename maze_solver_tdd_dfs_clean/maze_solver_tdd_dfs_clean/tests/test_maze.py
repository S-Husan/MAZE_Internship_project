import unittest

from maze import Maze


class TestMaze(unittest.TestCase):
    def test_find_start(self):
        grid = [
            ["#", "#", "#"],
            ["S", ".", "E"],
            ["#", "#", "#"],
        ]
        maze = Maze(grid)

        self.assertEqual(maze.find_start(), (1, 0))

    def test_find_end(self):
        grid = [
            ["#", "#", "#"],
            ["S", ".", "E"],
            ["#", "#", "#"],
        ]
        maze = Maze(grid)

        self.assertEqual(maze.find_end(), (1, 2))

    def test_get_neighbors_ignores_walls(self):
        grid = [
            ["#", "#", "#"],
            ["S", ".", "E"],
            ["#", "#", "#"],
        ]
        maze = Maze(grid)

        self.assertCountEqual(maze.get_neighbors(1, 1), [(1, 0), (1, 2)])

    def test_rejects_non_rectangular_maze(self):
        grid = [
            ["S", "."],
            [".", "E", "#"],
        ]

        with self.assertRaises(ValueError):
            Maze(grid)


if __name__ == "__main__":
    unittest.main()
