from random import randint, choice


class Sidewinder:

    @staticmethod
    def on(grid):
        for row in grid:
            run = []

            for cell in row:
                run.append(cell)

                at_eastern_boundary = (cell.east_neighbor is None)
                at_northern_boundary = (cell.north_neighbor is None)

                should_close_run = at_eastern_boundary or (not at_northern_boundary and randint(0, 2) == 0)

                if should_close_run:
                    random_run_cell = choice(run)
                    if random_run_cell.north_neighbor:
                        random_run_cell.link(random_run_cell.north_neighbor)
                    run.clear()
                else:
                    cell.link(cell.east_neighbor)

        return grid
