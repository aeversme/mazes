from grid import Grid
from binary_tree import BinaryTree


def create_maze():
    grid = Grid(4, 4)
    BinaryTree.on(grid.grid)
    return grid


def binary_tree_demo():
    maze = create_maze()
    print(maze.size())
    print(maze.grid)


if __name__ == "__main__":
    binary_tree_demo()
