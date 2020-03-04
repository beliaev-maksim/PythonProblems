import random
import cProfile


def main():
    # try:
    #     num_points = int(input("Amount of numbers, should be greater or equal than 20:\t"))
    # except ValueError:
    #     return print("Value is not an integer. Exit")
    #
    # if num_points < 20:
    #     return print("Number of points should be greater than 20. Exit")

    num_points = 30
    # generate random 2D coordinates, integers and limit by 100
    seq = []
    for i in range(num_points):
        seq.append(random.randint(0, 30))

    seq = [15, 0, 15, 14, 28, 1, 19, 28, 8, 8, 22, 5, 3, 18, 21, 3, 0, 9, 16, 29, 22, 8, 26, 5, 30, 0, 30, 24, 0, 21]
    print(seq)

    flag_first_zero = False
    flag_zero_found = False
    counter = 0
    for i, elem in enumerate(seq):
        if elem == 0:
            if flag_first_zero:
                print(sub_seq)
                counter += sum(sub_ind)
                flag_zero_found = True
            else:
                flag_first_zero = True

            sub_seq = []
            sub_ind = []
            continue

        if flag_first_zero:
            sub_seq.append(elem)
            sub_ind.append(i)

    if not flag_zero_found:
        print("No 2 zeros")
    else:
        print(counter)

    # alternative method
    for i in range(num_points):
        if seq[i] == 0:
            break

    if i == num_points - 1:
        return print("No zeros")

    sum_val = 0
    sum1 = 0
    n1 = i+1
    for j in range(i+1, num_points):
        if seq[j] != 0:
            sum1 += j
        else:
            sum_val += sum1
            sum1 = 0
            new_seq = []
            for k in range(n1, j):
                new_seq.append(seq[k])
            print(new_seq)
            n1 = j+1

    print(sum_val)


if __name__ == "__main__":
    cProfile.run("main()")
