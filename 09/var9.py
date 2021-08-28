import math
import random
import cProfile


def main():
    try:
        x = float(input("X of main point:\t"))
        y = float(input("Y of main point:\t"))
        z = float(input("Z of main point:\t"))
    except ValueError:
        return print("Value is not a number. Exit")

    main_point = [x, y, z]

    try:
        num_points = int(input("Number of points, should be greater or equal than 10:\t"))
    except ValueError:
        return print("Value is not an integer. Exit")

    if num_points < 10:
        return print("Number of points should be greater than 10. Exit")

    # generate random 3D coordinates, integers and limit by 100
    list_of_points = []
    for i in range(num_points):
        list_of_points.append([random.randint(0, 100),
                               random.randint(0, 100),
                               random.randint(0, 100)])

    print(list_of_points)

    list_of_vec = []
    for i, elem in enumerate(list_of_points):
        vec_1 = math.sqrt((main_point[0] - elem[0]) ** 2 +
                          (main_point[1] - elem[1]) ** 2 +
                          (main_point[2] - elem[2]) ** 2)
        list_of_vec.append(vec_1)

    add_val = 1 if len(list_of_vec) % 2 == 1 else 0
    middle_index = int(len(list_of_vec)/2) + add_val
    radius = sorted(list_of_vec)[middle_index]
    print("Radius:\t", radius)


if __name__ == "__main__":
    cProfile.run("main()")
