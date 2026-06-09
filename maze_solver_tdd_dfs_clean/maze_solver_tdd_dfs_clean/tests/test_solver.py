import unittest

from solver import solve_dfs, mark_solution


class TestSolver(unittest.TestCase):
    def test_dfs_finds_straight_path(self):
        maze = [["S", ".", "E"]]

        path = solve_dfs(maze)

        self.assertEqual(path, [(0, 0), (0, 1), (0, 2)])

    def test_dfs_finds_path_with_turns(self):
        maze = [
            ["#", "#", "#", "#", "#"],
            ["S", ".", ".", ".", "#"],
            ["#", "#", "#", ".", "#"],
            ["#", "E", ".", ".", "#"],
            ["#", "#", "#", "#", "#"],
        ]

        path = solve_dfs(maze)

        self.assertIsNotNone(path)
        self.assertEqual(path[0], (1, 0))
        self.assertEqual(path[-1], (3, 1))

    def test_dfs_returns_none_when_no_path_exists(self):
        maze = [["S", "#", "E"]]

        path = solve_dfs(maze)

        self.assertIsNone(path)

    def test_mark_solution_does_not_replace_start_or_end(self):
        maze = [["S", ".", "E"]]
        path = [(0, 0), (0, 1), (0, 2)]

        solved = mark_solution(maze, path)

        self.assertEqual(solved, [["S", "*", "E"]])


if __name__ == "__main__":
    unittest.main()
