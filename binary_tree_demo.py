from grid import Grid
from binary_tree import BinaryTree


def create_maze():
    grid = Grid(12, 12)
    BinaryTree.on(grid.grid)
    return grid


def binary_tree_demo():
    maze = create_maze()
    print(maze)


if __name__ == "__main__":
    binary_tree_demo()
