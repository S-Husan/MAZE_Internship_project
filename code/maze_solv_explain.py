# This opens the maze.txt file.
# encoding="utf8" is used because the maze contains special characters like █ and ●.
with open("maze.txt", encoding="utf8") as f:

    # This reads every line from the file.
    #
    # line.rstrip("\n") removes the newline character at the end of each line.
    #
    # list(...) turns each line into a list of characters.
    #
    # Example:
    # "S   █" becomes ["S", " ", " ", " ", "█"]
    maze = [list(line.rstrip("\n")) for line in f]


# H means height of the maze.
# len(maze) counts how many rows there are.
H = len(maze)

# W means width of the maze.
# len(maze[0]) counts how many characters are in the first row.
W = len(maze[0])


# start will store the position of "S".
# At first, we do not know where it is, so it is None.
start = None

# end will store the position of "E".
# At first, we do not know where it is, so it is None.
end = None


# This loop goes through every row number.
# y is the row index.
for y in range(H):

    # This loop goes through every column number.
    # x is the column index.
    for x in range(W):

        # If the current maze cell is "S",
        # then we found the starting position.
        if maze[y][x] == "S":

            # We save the start position as (x, y).
            # x comes first, y comes second.
            start = (x, y)

        # If the current maze cell is "E",
        # then we found the ending position.
        elif maze[y][x] == "E":

            # We save the end position as (x, y).
            end = (x, y)


# visited is a set.
# It stores all cells that DFS already checked.
# This prevents the solver from going in circles forever.
visited = set()

# solution is a list.
# It stores the current path that DFS is trying.
solution = []


# This function tries to find a path from the current position to the end.
# x is the current horizontal position.
# y is the current vertical position.
def dfs(x, y):

    # If this position was already visited,
    # we do not need to check it again.
    if (x, y) in visited:

        # False means this path does not work.
        return False

    # If the current cell is a wall,
    # we cannot walk through it.
    if maze[y][x] == "█":

        # False means this path does not work.
        return False

    # We mark this position as visited.
    # This means DFS has already checked this cell.
    visited.add((x, y))

    # We add this position to the current solution path.
    solution.append((x, y))

    # If the current position is the ending position,
    # we found the correct path.
    if (x, y) == end:

        # True means the path is found.
        return True

    # These are the four directions DFS can move.
    #
    # (1, 0) means move right.
    # (-1, 0) means move left.
    # (0, 1) means move down.
    # (0, -1) means move up.
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

        # nx means next x position.
        # ny means next y position.
        nx, ny = x + dx, y + dy

        # This checks if the next position is inside the maze.
        #
        # 0 <= nx means it is not outside the left side.
        # nx < W means it is not outside the right side.
        # 0 <= ny means it is not outside the top side.
        # ny < H means it is not outside the bottom side.
        if 0 <= nx < W and 0 <= ny < H:

            # This calls DFS again from the next position.
            # If DFS from the next position finds the end,
            # then we also return True.
            if dfs(nx, ny):

                # True means the correct path has been found.
                return True

    # If none of the directions worked,
    # this cell is not part of the final solution.
    #
    # So we remove it from the solution path.
    solution.pop()

    # False means this path failed.
    return False


# This starts DFS from the start position.
# start[0] is the x position of S.
# start[1] is the y position of S.
dfs(start[0], start[1])


# This loop goes through every position in the final solution path.
for x, y in solution:

    # We do not replace "S" or "E".
    # We only put dots on empty path cells.
    if maze[y][x] not in ("S", "E"):

        # This marks the correct path with a dot.
        maze[y][x] = "●"


# This prints an empty line, then the title.
print("\nSolved Maze:\n")

# This goes through every row in the maze.
for row in maze:

    # This prints the row on the terminal.
    # "".join(row) changes the list of characters into one string.
    print("".join(row))