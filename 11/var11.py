import cProfile
import random

DIMENSION = 20


def main():
    list_a = []
    list_b = []
    for i in range(DIMENSION):
        list_a.append(random.randint(1, 30))
        list_b.append(random.randint(1, 30))

    print("A:\t", list_a)
    print("B:\t", list_b)

    list_c = sorted(list_a + list_b)
    print("C (not filtered):\t", list_c)

    counter = 0
    index_delete = []
    for i, elem in enumerate(list_c):
        try:
            if elem == list_c[i+1]:
                counter += 1
                if counter >= 2:
                    index_delete.append(i)
            else:
                counter = 0
        except IndexError:
            pass

    # reverse index list because otherwise we will shift all index in list_c while pop
    for elem in index_delete[::-1]:
        list_c.pop(elem)

    print("C (filtered):\t\t", list_c)

    harmonic_mean = len(list_c) / sum([1/elem for elem in list_c])
    print("Harmonic mean:\t", harmonic_mean)


if __name__ == "__main__":
    cProfile.run("main()")
