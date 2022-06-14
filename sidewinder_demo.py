from grid import Grid
from sidewinder import Sidewinder
from secrets import token_hex


def create_maze():
    grid = Grid(12, 12)
    Sidewinder.on(grid.grid)
    return grid


def sidewinder_demo():
    maze = create_maze()
    random_hex = token_hex(4)
    print(maze)
    print(f'Maze number {random_hex}')
    image = maze.to_png()
    image.save(f'images/sidewinder-{random_hex}.png')


if __name__ == '__main__':
    sidewinder_demo()
