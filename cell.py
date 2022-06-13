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
        """
        Takes a Cell object. Sets the object as a key in the self.links dictionary with a value of True.
        :param cell: Cell object
        :param bidi: boolean
        :return: dictionary
        """
        self.links[cell] = True
        if bidi:
            cell.link(self, False)
        return self.links

    def unlink(self, cell, bidi=True):
        """
        Takes a Cell object. If the object is a key in the self.links dictionary, removes the key and value from the
        dictionary.
        :param cell: Cell object
        :param bidi: boolean
        :return: dictionary
        """
        try:
            self.links.pop(cell)
        except KeyError:
            pass
        if bidi:
            cell.unlink(self, False)
        return self.links

    def show_links(self):
        """
        Returns a list of keys in the self.links dictionary.
        :return: list
        """
        return [item_key for item_key in self.links]

    def is_linked(self, cell):
        """
        Takes a Cell object. If the object is a key in the self.links dictionary, returns True. Otherwise,
        returns False.
        :param cell: Cell object
        :return: boolean
        """
        if cell in self.links.keys():
            return True
        return False

    def neighbors(self):
        """
        Returns a list of Cell objects that are immediately adjacent to the current Cell object.
        :return: list
        """
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
