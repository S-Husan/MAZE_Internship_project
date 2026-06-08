with open("maze.txt", encoding="utf8") as f:
    maze = [list(line.rstrip("\n")) for line in f]

H = len(maze)
W = len(maze[0])

start = None
end = None

for y in range(H):
    for x in range(W):
        if maze[y][x] == "S":
            start = (x, y)
        elif maze[y][x] == "E":
            end = (x, y)

visited = set()
solution = []


def dfs(x, y):
    if (x, y) in visited:
        return False

    if maze[y][x] == "█":
        return False

    visited.add((x, y))
    solution.append((x, y))

    if (x, y) == end:
        return True

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < W and 0 <= ny < H:
            if dfs(nx, ny):
                return True

    solution.pop()
    return False


dfs(start[0], start[1])

for x, y in solution:
    if maze[y][x] not in ("S", "E"):
        maze[y][x] = "●"

print("\nSolved Maze:\n")
for row in maze:
    print("".join(row))
    