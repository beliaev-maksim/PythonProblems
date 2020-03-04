import cProfile
import random

DIMENSION = 10
PRIME_NUMBER_LIST = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def main():
    list_2d = []
    for i in range(DIMENSION):
        list_2d.append([])
        for j in range(DIMENSION):
            list_2d[i].append(random.randint(0, 100))

    max_val = -1e9
    multiple = 1.0  # keep it float to avoid overflow during int->float conversion for big numbers
    n = 0

    list_2d_reversed = []
    for i in range(DIMENSION):
        list_2d_reversed.append([])
        for j in range(DIMENSION):
            val = list_2d[j][i]
            list_2d_reversed[i].append(val)

            # let's avoid another one looping and calculate here
            if val in PRIME_NUMBER_LIST:
                multiple *= val
                n += 1
                if val > max_val:
                    max_val = val

    print("Matrix initial:")
    for row in list_2d:
        print(row)

    print("Matrix reversed:")
    for row in list_2d_reversed:
        print(row)

    geometrical_mean = multiple ** (1/n)
    print("Geometrical mean:\t", geometrical_mean)
    print("Max prime number:\t", max_val)


if __name__ == "__main__":
    cProfile.run("main()")
