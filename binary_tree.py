from random import choice


class BinaryTree:

    @staticmethod
    def on(grid):
        for row in grid:
            for cell in row:
                neighbors = []
                if cell.north_neighbor:
                    neighbors.append(cell.north_neighbor)
                if cell.east_neighbor:
                    neighbors.append(cell.east_neighbor)

                try:
                    neighbor = choice(neighbors)
                except IndexError:
                    neighbor = None

                if neighbor:
                    cell.link(neighbor)
        return grid
