import random

WIDTH = 41
HEIGHT = 21

maze = [["█" for _ in range(WIDTH)] for _ in range(HEIGHT)]


def generate(x, y):
    maze[y][x] = " "

    dirs = [(0, -2), (2, 0), (0, 2), (-2, 0)]
    random.shuffle(dirs)

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 1 <= nx < WIDTH - 1 and 1 <= ny < HEIGHT - 1:
            if maze[ny][nx] == "█":
                maze[y + dy // 2][x + dx // 2] = " "
                generate(nx, ny)


generate(1, 1)

maze[1][0] = "S"
maze[HEIGHT - 2][WIDTH - 2] = "E"

with open("maze.txt", "w", encoding="utf8") as f:
    for row in maze:
        f.write("".join(row) + "\n")

print("\nGenerated Maze:\n")
for row in maze:
    print("".join(row))