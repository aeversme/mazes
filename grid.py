from cell import Cell
from random import randint
from PIL import Image, ImageDraw


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

    def __str__(self):
        output = '+' + (' \U00002500\U00002500\U00002500 +' * self.columns) + '\n'
        for row in self.grid:
            top = '\U00002502'
            bottom = '+'
            for cell in row:
                if not cell:
                    cell = Cell(-1, -1)

                body = '     '
                corner = '+'

                east_boundary = ' ' if cell.is_linked(cell.east_neighbor) else '\U00002502'
                top = top + body + east_boundary

                south_boundary = '     ' if cell.is_linked(cell.south_neighbor) else ' \U00002500\U00002500\U00002500 '
                bottom = bottom + south_boundary + corner

            output = output + top + '\n' + bottom + '\n'

        return output

    def to_png(self, cell_size=40):
        img_height = cell_size * self.rows
        img_width = cell_size * self.columns

        white = (255, 255, 255)
        black = (0, 0, 0)

        image = Image.new('RGB', (img_width + 1, img_height + 1), white)
        draw = ImageDraw.Draw(image)

        for row in self.grid:
            for cell in row:
                x1 = cell.column * cell_size
                y1 = cell.row * cell_size

                x2 = (cell.column + 1) * cell_size
                y2 = (cell.row + 1) * cell_size

                if not cell.north_neighbor:
                    draw.line((x1, y1, x2, y1), fill=black, width=1)
                if not cell.west_neighbor:
                    draw.line((x1, y1, x1, y2), fill=black, width=1)

                if not cell.is_linked(cell.east_neighbor):
                    draw.line((x2, y1, x2, y2), fill=black, width=1)
                if not cell.is_linked(cell.south_neighbor):
                    draw.line((x1, y2, x2, y2), fill=black, width=1)

        return image
