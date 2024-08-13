import numpy as np
import itertools


def accumulate_path(matrix):
    rows, cols = matrix.shape
    accumulated = np.zeros((rows, cols))
    accumulated[0, :] = list(itertools.accumulate(matrix[0, :]))
    accumulated[:, 0] = list(itertools.accumulate(matrix[:, 0]))
    for i in range(1, rows):
        for j in range(1, cols):
            accumulated[i, j] = matrix[i, j] + max(
                accumulated[i, j - 1], accumulated[i - 1, j - 1], accumulated[i - 1, j])
    return accumulated


def traceback_path(matrix):
    traceback_indices = []
    f_matrix = accumulate_path(matrix)
    i, j = f_matrix.shape[0] - 1, f_matrix.shape[1] - 1
    while i > 0 or j > 0:
        traceback_indices.append((i, j))
        if f_matrix[i, j] == matrix[i, j] + f_matrix[i - 1, j - 1]:
            i -= 1
            j -= 1
        elif f_matrix[i, j] == matrix[i, j] + f_matrix[i - 1, j]:
            i -= 1
        else:
            j -= 1
    traceback_indices.append((0, 0))
    return traceback_indices


def path_array(traceback_indices):
    rows, cols = traceback_indices[0]
    return np.array([[1 if (i, j) in traceback_indices else 0 for j in range(cols + 1)] for i in range(rows + 1)])


def main():
    arr = np.random.randint(low=-10, high=10, size=(5, 5))
    print(f'Matrix: \n{arr}\n')
    print(f'Cumulative path sum to each cell: \n{accumulate_path(arr)}\n')
    tb_indices = traceback_path(arr)
    print(f'Set of indices that give the optimal path: \n{tb_indices}\n')
    path = path_array(tb_indices)
    print(f'Path matrix: \n{path}\n')
    print(f'Result: \n{np.sum(path * arr)}\n')
    return 0


if __name__ == '__main__':
    main()
