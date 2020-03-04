import random
import cProfile
import json

def main():
    # try:
    #     num_points = int(input("Amount of numbers, should be greater or equal than 20:\t"))
    # except ValueError:
    #     return print("Value is not an integer. Exit")
    #
    # if num_points < 20:
    #     return print("Number of points should be greater than 20. Exit")

    num_points = 10000000
    # generate random 2D coordinates, integers and limit by 100
    seq = []
    for i in range(num_points):
        seq.append(random.randint(0, 30))

    # print(seq)
    with open("D:\\1.txt", "w") as file:
        json.dump({"seq": seq}, file)
    return
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
            # print(new_seq)
            n1 = j+1

    print(sum_val)


if __name__ == "__main__":
    cProfile.run("main()")
