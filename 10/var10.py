import cProfile
import random

DIMENSION = 10


def main():
    """
    In this function we create a 2D list of random values, then we reverse rows and columns.
    Find the smallest sum of element in the row (of new reversed matrix). After that we change sequence of
    rows (mirroring) around smallest row. Finally we reverse matrix back.
    """
    list_2d = []
    for i in range(DIMENSION):
        list_2d.append([])
        for j in range(DIMENSION):
            list_2d[i].append(random.randint(0, 100))

    print("Matrix initial:")
    for row in list_2d:
        print(row)

    reversed_list = reverse_matrix(list_2d)
    smallest = 1e9
    smallest_index = 0
    for i, elem in enumerate(reversed_list):
        sum_of_elem = sum(elem)
        if sum_of_elem < smallest:
            smallest = sum_of_elem
            smallest_index = i

    smallest_column = reversed_list.pop(smallest_index)
    print("Smallest column:\t", smallest_column)

    mirrored_list = reversed_list[::-1]
    mirrored_list.insert(len(mirrored_list)-smallest_index, smallest_column)

    final_list = reverse_matrix(mirrored_list)
    print("Matrix mirrored:")
    for row in final_list:
        print(row)

    root_mean_sq = (sum([elem**2 for elem in smallest_column]) / len(smallest_column)) ** 0.5
    print("Root mean square:\t", root_mean_sq)


def reverse_matrix(matrix):
    """Function to reverse matrix - exchange rows and columns
    :param matrix: (list) input 2d list to reverse
    :return reversed 2d list"""
    list_2d_reversed = []
    for i in range(DIMENSION):
        list_2d_reversed.append([])
        for j in range(DIMENSION):
            val = matrix[j][i]
            list_2d_reversed[i].append(val)

    return list_2d_reversed


if __name__ == "__main__":
    print(help(reverse_matrix))
    cProfile.run("main()")
