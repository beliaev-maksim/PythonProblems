import cProfile
import random

DIMENSION = 5


def main():
    list_a = []
    for i in range(DIMENSION):
        list_a.append([])
        for j in range(DIMENSION):
            list_a[i].append(random.randint(0, 10))

    print("A:\t", list_a)

    try:
        seq = input("Type sequence of number 1-10, comma separated." +
                    "Number of elements should be equal to {}:\t".format(DIMENSION))
        list_b = [int(elem) for elem in seq.split(",")]
    except ValueError:
        return print("Value is not a number. Exit")

    for elem in list_b:
        if not 1 <= elem <= 10:
            return print("All points should be in range 1-10. Exit")

    if len(list_b) != DIMENSION:
        return print("Number of elements should be DIMENSION. Exit")

    list_c = []

    for i in range(DIMENSION):
        list_c.append([])
        for j in range(DIMENSION):
            list_c[i].append(list_a[i][j] * list_b[j] ** i)

    print("C:\t", list_c)


if __name__ == "__main__":
    cProfile.run("main()")