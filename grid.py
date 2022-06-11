from cell import Cell
from random import randint


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells(self.grid)

    def prepare_grid(self):
        """
        Creates a two-dimensional list of Cell objects.
        :return: list
        """
        grid = []
        for row in self.rows:
            new_row = []
            for column in self.columns:
                new_row.append(Cell(row, column))
            grid.append(new_row)
        return grid

    @staticmethod
    def configure_cells(grid):
        """
        Iterates through a grid and assigns neighbors to each Cell object in the grid.
        :param grid: list
        :return: None
        """
        for r in grid:
            for cell in r:
                row, column = cell.row, cell.column

                cell.north_neighbor = grid[row - 1][column]
                cell.south_neighbor = grid[row + 1][column]
                cell.west_neighbor = grid[row][column - 1]
                cell.east_neighbor = grid[row][column + 1]

    def grid_accessor(self, row, column):
        """
        Returns a Cell object, or None if one of the parameters is outside the grid boundaries.
        :param row: int
        :param column: int
        :return: None, or Cell object
        """
        if 0 <= row <= self.rows - 1 or 0 <= column <= len(self.grid[row]) - 1:
            return self.grid[row][column]
        return None

    def random_cell(self):
        """
        Returns a random Cell object from the grid.
        :return: Cell object
        """
        row = randint(0, len(self.grid) - 1)
        column = randint(0, len(self.grid[row]) - 1)
        return self.grid[row][column]

    def size(self):
        """
        Returns the area of the grid.
        :return: int
        """
        return self.rows * self.columns
