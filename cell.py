class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = {}
        self.north_neighbor = None
        self.south_neighbor = None
        self.east_neighbor = None
        self.west_neighbor = None

    def __repr__(self):
        return f"Cell R{self.row} C{self.column}"

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)
        return self.links

    def unlink(self, cell, bidi=True):
        self.links.pop(cell)
        if bidi:
            cell.unlink(self, False)
        return self.links

    def show_links(self):
        return self.links.keys()

    def is_linked(self, cell):
        if cell in self.links.keys():
            return True
        return False

    def neighbors(self):
        neighbor_list = []
        if self.north_neighbor:
            list.append(neighbor_list, self.north_neighbor)
        if self.south_neighbor:
            list.append(neighbor_list, self.south_neighbor)
        if self.east_neighbor:
            list.append(neighbor_list, self.east_neighbor)
        if self.west_neighbor:
            list.append(neighbor_list, self.west_neighbor)
        return neighbor_list
