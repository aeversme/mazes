from cell import Cell
from random import randint


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells(self.grid)

    def prepare_grid(self):
        grid = []
        for row in self.rows:
            new_row = []
            for column in self.columns:
                new_row.append(Cell(row, column))
            grid.append(new_row)
        return grid

    @staticmethod
    def configure_cells(grid):
        for r in grid:
            for cell in r:
                row, column = cell.row, cell.column

                cell.north_neighbor = grid[row - 1][column]
                cell.south_neighbor = grid[row + 1][column]
                cell.west_neighbor = grid[row][column - 1]
                cell.east_neighbor = grid[row][column + 1]

    def grid_accessor(self, row, column):
        if 0 <= row <= self.rows - 1 or 0 <= column <= len(self.grid[row]) - 1:
            return self.grid[row][column]
        return None

    def random_cell(self):
        row = randint(0, len(self.grid) - 1)
        column = randint(0, len(self.grid[row]) - 1)
        return self.grid[row][column]

    def size(self):
        return self.rows * self.columns
