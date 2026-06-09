# MAZE_Internship_project
# DFS Maze Solver Project — TDD Version

This version keeps the project simple:

- DFS maze generator
- DFS maze solver
- No BFS
- No animation
- Unit tests for TDD
- Terminal output

## Files

```text
maze.py              Maze helper class
generator.py         DFS recursive-backtracking maze generator
solver.py            DFS maze solver
loader.py            Save/load maze.txt
renderer.py          Terminal rendering
create_maze.py       Generate maze.txt and print it
solve_maze.py        Solve maze.txt and print only final correct path
main.py              Small menu
tests/test_maze.py
tests/test_generator.py
tests/test_solver.py
```

## Run tests first

```bash
python -m unittest discover -s tests
```

## Generate a maze

```bash
python create_maze.py
```

## Solve the maze with DFS

```bash
python solve_maze.py
```

## Optional menu

```bash
python main.py
```

## TDD idea used here

1. Write tests for the maze model.
2. Write tests for DFS solving.
3. Write tests proving generated mazes have `S`, `E`, correct size, and are solvable.
4. Write the code until all tests pass.
