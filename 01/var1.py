import random


def main():
    list_2d = []
    for i in range(10):
        list_2d.append([])
        for j in range(10):
            list_2d[i].append(random.randint(0, 10))

    print(list_2d)

    try:
        x_value = int(input("Type an integer number in range [0-10]:  "))
    except ValueError:
        return print("Value is not an integer. Exit")

    if not 0 <= x_value <= 10:
        return print("Value should be in range [0-10]. Exit")

    for array in list_2d:
        for i, elem in enumerate(array):
            if elem == x_value:
                array[i] = elem**2
            elif elem < x_value:
                array[i] = elem**x_value
            else:
                array[i] = elem * 2

    print("New list: ", list_2d)


if __name__ == "__main__":
    main()
