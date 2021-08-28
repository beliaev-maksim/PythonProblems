import random
import cProfile
import math


def main():
    list_2d = []
    for i in range(4):
        list_2d.append([random.randint(0, 16),
                        random.randint(0, 16),
                        random.randint(0, 16),
                        random.randint(0, 16)])

    print(list_2d)

    sum_val = 0
    counter_list = [0]*17  # initialize list with 7 zeros
    for elem in list_2d:
        for num in elem:
            counter_list[num] += 1
            sum_val += num

    squared_elem = [elem**2 for elem in counter_list]
    mean_val = math.sqrt(sum(squared_elem) / len(counter_list))

    print("List of numbers count:\t", counter_list)
    print("This value is most frequent:\t", counter_list.index(max(counter_list)))
    print("Sum of elements:\t", sum_val)
    print("Mean value:\t", mean_val)


if __name__ == "__main__":
    cProfile.run("main()")
