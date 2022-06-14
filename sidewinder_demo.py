from grid import Grid
from sidewinder import Sidewinder


def create_maze():
    grid = Grid(12, 12)
    Sidewinder.on(grid.grid)
    return grid


def sidewinder_demo():
    maze = create_maze()
    print(maze)


if __name__ == '__main__':
    sidewinder_demo()
