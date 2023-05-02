import numpy as np
import sys

np.set_printoptions(suppress=True, linewidth=np.nan, threshold=sys.maxsize)


def create_mat(rows, *cols):
    if len(cols) == 0:
        cols = rows
    else:
        cols = int(cols[0])
    return np.random.randint(2, size=(rows, cols))


def neighborCount(matrix):
    tmp = matrix[1][1]  # store middle point
    matrix[1][1] = 0  # set middle point to zero
    n_neighbors = np.sum(matrix)  # sum up all neighbors
    matrix[1][1] = tmp  # restore middle point
    return n_neighbors


def get_neighbors(universe):
    universe_dim = universe.shape  # shape of universe/game field
    universe_expand = np.tile(universe, (3, 3))  # expand matrix
    universe_expand = universe_expand[universe_dim[0] - 1:-(universe_dim[0] - 1), universe_dim[1] - 1:-(universe_dim[1] - 1)]  # delete outer rows and cols
    neighbors_mat = np.zeros(universe_dim, dtype=int)  # init zero matrix

    for row in range(0, universe_dim[0]):
        for col in range(0, universe_dim[1]):
            neighbors_mat[row][col] = neighborCount(universe_expand[row:row + 3, col:col + 3])  # get sum of chunk

    return neighbors_mat


def display(universe):
    disp_uni = np.where(universe > 0, "*", " ")
    disp_uni = str(disp_uni).replace("'", '')
    return disp_uni


def dead_alive(universe, neighbors):

    new_universe = np.where((universe == 0) & (neighbors == 3) |
                            ((universe == 1) & ((neighbors == 3) | (neighbors == 2))),
                            1, 0)

    new_neighbors = get_neighbors(new_universe)
    new_display = display(new_universe)

    return new_universe, new_neighbors, new_display
