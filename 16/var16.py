import cProfile
import random

DIMENSION = 10


def main():
    list_2d = []
    for i in range(DIMENSION):
        list_2d.append([])
        for j in range(DIMENSION):
            list_2d[i].append(random.randint(1, 100))

    print("Matrix initial:")
    for row in list_2d:
        print(row)
    print("\n\n")

    count_list = []
    # make step of 2 because we need 2x2 matrices
    for i in range(0, DIMENSION, 2):
        for j in range(0, DIMENSION, 2):
            sum_val = list_2d[i][j] + list_2d[i][j+1] + list_2d[i+1][j] + list_2d[i+1][j+1]

            count_list.append([sum_val,
                               [list_2d[i][j], list_2d[i][j+1]],
                               [list_2d[i+1][j], list_2d[i+1][j+1]]])

    # sort by the first value where we save the sum of elements
    count_list.sort(key=lambda x: x[0])

    for elem in count_list:
        print(elem[1])
        print(elem[2], "\n\n")

    geometrical_mean = DIMENSION/2 / sum(1/x for x in [elem[0] for elem in count_list])
    print("Geometrical mean:\t", geometrical_mean)


if __name__ == "__main__":
    cProfile.run("main()")
