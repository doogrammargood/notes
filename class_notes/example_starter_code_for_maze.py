import random
import os

WALL = "█"
PATH = " "
PLAYER = "P"
EXIT = "E"

WIDTH = 21   # must be odd
HEIGHT = 11  # must be odd


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def generate_maze(width, height):
    maze = [[WALL for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1:
                if maze[ny][nx] == WALL:
                    maze[ny][nx] = PATH
                    maze[y + dy // 2][x + dx // 2] = PATH
                    carve(nx, ny)

    maze[1][1] = PATH
    carve(1, 1)
    return maze


def draw_maze(maze, px, py):
    clear()
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if x == px and y == py:
                print(PLAYER, end="")
            else:
                print(cell, end="")
        print()


def game():
    maze = generate_maze(WIDTH, HEIGHT)

    px, py = 1, 1
    ex, ey = WIDTH - 2, HEIGHT - 2
    maze[ey][ex] = EXIT

    while True:
        draw_maze(maze, px, py)

        if (px, py) == (ex, ey):
            print("\n🎉 You escaped the maze!")
            break

        move = input("Move (WASD, Q to quit): ").lower()
        if move == "q":
            break

        dx, dy = 0, 0
        if move == "w":
            dy = -1
        elif move == "s":
            dy = 1
        elif move == "a":
            dx = -1
        elif move == "d":
            dx = 1

        nx, ny = px + dx, py + dy
        if maze[ny][nx] != WALL:
            px, py = nx, ny


if __name__ == "__main__":
    game()
