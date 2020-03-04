import cProfile


def main():
    try:
        seq = input("Type sequence of number 1-10, comma separated. Number of elements should be even:\t")
        list_of_num = [int(elem) for elem in seq.split(",")]
    except ValueError:
        return print("Value is not a number. Exit")

    for elem in list_of_num:
        if not 1 <= elem <= 10:
            return print("All points should be in range 1-10. Exit")

    if len(list_of_num) % 2 != 0:
        return print("Number of elements should be even. Exit")

    multiple_val = 1
    for elem in list_of_num:
        multiple_val *= elem

    geometric_mean = pow(multiple_val, 1/len(list_of_num))  # power of 1/n equal to root of n
    print(geometric_mean)

    list_of_num.sort()
    sorted_list = []
    while list_of_num:
        min_val = list_of_num.pop(0)
        max_val = list_of_num.pop(len(list_of_num)-1)
        sorted_list.append(min_val)
        sorted_list.append(max_val)

    print(sorted_list)


if __name__ == "__main__":
    cProfile.run("main()")
