import sys


def next(pattern):
    return survivors_cells(pattern) + come_to_life(pattern)


# rules of game
def cell_survives(cells, cell):
    neighbours = living_neighbours(cells, cell)
    return neighbours == 2 or neighbours == 3


def cell_comes_to_life(cells, cell):
    return living_neighbours(cells, cell) == 3


def get_neighbours(x, y):
    return [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    ]
def living_neighbours(cells, cell):
    x, y = cell
    potential_neighbours = get_neighbours(x, y)
    return len(set(potential_neighbours).intersection(cells))


def survivors_cells(cells):
    return [cell for cell in cells if cell_survives(cells, cell)]


def come_to_life(last_generation):
    candidates = might_come_to_life(last_generation)
    return [cell for cell in candidates if living_neighbours(last_generation, cell) == 3]


def might_come_to_life(last_generation):
    n = [get_neighbours(x, y) for (x, y) in last_generation]
    touching_live_cells = []
    for these_neighbours in n:
        touching_live_cells += these_neighbours
    return set(touching_live_cells).difference(last_generation)


test = ([(10,10),(10,11),(11,10),(11,11)])
test = test
one = next(test)
two = next(one)
three = next(two)

print test
print one
print two
print three
