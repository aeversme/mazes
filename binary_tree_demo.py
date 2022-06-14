from grid import Grid
from binary_tree import BinaryTree
from secrets import token_hex


def create_maze():
    grid = Grid(12, 12)
    BinaryTree.on(grid.grid)
    return grid


def binary_tree_demo():
    maze = create_maze()
    random_hex = token_hex(4)
    print(maze)
    print(f'Maze number {random_hex}')
    image = maze.to_png()
    image.save(f'images/bin-tree-{random_hex}.png')


if __name__ == "__main__":
    binary_tree_demo()
