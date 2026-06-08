# We import the random module because we need to shuffle directions randomly.
# This makes the maze different every time we run the program.
import random


# WIDTH means how many characters wide the maze will be.
# 41 is an odd number, which is good for this maze algorithm.
WIDTH = 41

# HEIGHT means how many lines tall the maze will be.
# 21 is also an odd number, which is good for this maze algorithm.
HEIGHT = 21


# This creates the maze grid.
# maze is a list of rows.
# Each row is also a list.
# At the beginning, every cell is a wall: "█"
maze = [["█" for _ in range(WIDTH)] for _ in range(HEIGHT)]


# This function makes the maze using DFS.
# x is the current horizontal position.
# y is the current vertical position.
def generate(x, y):

    # We make the current cell empty.
    # Empty space means the player can walk here.
    maze[y][x] = " "

    # These are the four possible directions.
    # We move by 2 cells because between maze rooms there is a wall.
    #
    # (0, -2) means move up.
    # (2, 0) means move right.
    # (0, 2) means move down.
    # (-2, 0) means move left.
    dirs = [(0, -2), (2, 0), (0, 2), (-2, 0)]

    # This changes the order of directions randomly.
    # Because of this, every generated maze looks different.
    random.shuffle(dirs)

    # We check every direction one by one.
    for dx, dy in dirs:

        # nx means new x position.
        # ny means new y position.
        #
        # dx is added to x.
        # dy is added to y.
        nx, ny = x + dx, y + dy

        # This checks if the new position is inside the maze.
        #
        # 1 <= nx means we do not go outside the left wall.
        # nx < WIDTH - 1 means we do not go outside the right wall.
        # 1 <= ny means we do not go outside the top wall.
        # ny < HEIGHT - 1 means we do not go outside the bottom wall.
        if 1 <= nx < WIDTH - 1 and 1 <= ny < HEIGHT - 1:

            # This checks if the new cell is still a wall.
            # If it is a wall, it means we have not visited it yet.
            if maze[ny][nx] == "█":

                # This removes the wall between the current cell and the new cell.
                #
                # dy // 2 gives the middle y position.
                # dx // 2 gives the middle x position.
                #
                # Example:
                # If we move right by 2 cells, dx is 2.
                # dx // 2 is 1, so we remove the wall 1 cell to the right.
                maze[y + dy // 2][x + dx // 2] = " "

                # Now we continue generating the maze from the new cell.
                # This is recursion.
                # The function calls itself.
                generate(nx, ny)


# This starts maze generation from position x=1, y=1.
# We do not start from 0 because 0 is the outside wall.
generate(1, 1)


# This creates the start point.
# maze[1][0] means row 1, column 0.
# This puts "S" on the left side of the maze.
maze[1][0] = "S"

# This creates the ending point.
# HEIGHT - 2 means one row before the bottom wall.
# WIDTH - 2 means one column before the right wall.
# This puts "E" near the bottom-right side.
maze[HEIGHT - 2][WIDTH - 2] = "E"


# This opens a file called maze.txt.
# "w" means write mode.
# encoding="utf8" is used because we use special characters like █.
with open("maze.txt", "w", encoding="utf8") as f:

    # This goes through every row in the maze.
    for row in maze:

        # "".join(row) changes the list of characters into one string.
        # "\n" adds a new line after each row.
        # f.write saves that row into maze.txt.
        f.write("".join(row) + "\n")


# This prints an empty line, then the title.
print("\nGenerated Maze:\n")

# This goes through every row in the maze.
for row in maze:

    # This prints the row on the terminal.
    # "".join(row) changes the list into text.
    print("".join(row))