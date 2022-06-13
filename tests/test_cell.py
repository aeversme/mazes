import pytest

from ..cell import Cell


def setup(link=False):
    cell1 = Cell(1, 2)
    cell2 = Cell(3, 4)
    if link:
        cell1.link(cell2)
    return cell1, cell2


def test_cell_initialization():
    cell1, cell2 = setup()

    assert cell1.__repr__() == 'Cell R1 C2'
    assert cell2.row == 3
    assert cell2.column == 4


def test_cell_link():
    cell1, cell2 = setup(link=True)

    assert cell1.links[cell2]


def test_cell_unlink():
    cell1, cell2 = setup(link=True)

    cell1.unlink(cell2)

    with pytest.raises(KeyError):
        link = cell1.links[cell2]


def test_cell_show_links():
    cell1, cell2 = setup(link=True)

    cell3 = Cell(5, 6)
    cell1.link(cell3)

    keys = cell1.show_links()

    assert len(keys) == 2
    assert keys[0].__repr__() == 'Cell R3 C4'


def test_cell_is_linked():
    cell1, cell2 = setup(link=True)

    assert cell1.is_linked(cell2)


def test_cell_neighbors():
    cell1, cell2 = setup()
    cell3 = Cell(5, 6)

    cell1.north_neighbor = cell2
    cell1.west_neighbor = cell3
    neighbors = cell1.neighbors()

    assert len(neighbors) == 2
    assert neighbors[0].__repr__() == 'Cell R3 C4'
    assert neighbors[1].__repr__() == 'Cell R5 C6'
    assert cell1.east_neighbor is None
