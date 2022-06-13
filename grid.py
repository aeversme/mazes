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
        for r in range(self.rows):
            new_row = []
            for c in range(self.columns):
                new_row.append(Cell(r, c))
            grid.append(new_row)
        return grid

    def configure_cells(self, grid):
        """
        Iterates through a grid and assigns neighbors to each Cell object in the grid.
        :param grid: list
        :return: None
        """
        for r in grid:
            for cell in r:
                row, column = cell.row, cell.column

                cell.north_neighbor = self.array_lookup(row - 1, column)
                cell.south_neighbor = self.array_lookup(row + 1, column)
                cell.west_neighbor = self.array_lookup(row, column - 1)
                cell.east_neighbor = self.array_lookup(row, column + 1)

    def array_lookup(self, row, column):
        """
        Returns a Cell object, or None if one of the parameters is outside the grid boundaries.
        :param row: int
        :param column: int
        :return: None, or Cell object
        """
        if row < 0 or row > (self.rows - 1) or column < 0 or column > (len(self.grid[row]) - 1):
            return None
        return self.grid[row][column]

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
