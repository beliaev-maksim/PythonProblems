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
    vec_long = -1
    for i, elem in enumerate(list_of_points):
        vec_1 = math.sqrt((main_point[0] - elem[0]) ** 2 +
                          (main_point[1] - elem[1]) ** 2 +
                          (main_point[2] - elem[2]) ** 2)
        list_of_vec.append(vec_1)
        if vec_1 > vec_long:
            vec_long = vec_1
            farthest_point = elem

    # for each pair of points calculate length between them and calculate perimeter
    # only if perimeter greater than previous one override it and override points variables
    perimeter_small = -1
    point1 = farthest_point
    point2 = None
    for i, elem in enumerate(list_of_points):
        # calculate length between two points
        vec_3 = math.sqrt((elem[0] - farthest_point[0]) ** 2 +
                          (elem[1] - farthest_point[1]) ** 2 +
                          (elem[2] - farthest_point[2]) ** 2)
        perimeter = list_of_vec[i] + vec_long + vec_3

        if perimeter > perimeter_small:
            perimeter_small = perimeter
            point2 = elem

    print("Perimeter:\t", perimeter_small)
    print("Point 1:\t", point1, "\nPoint 2:\t", point2)


if __name__ == "__main__":
    cProfile.run("main()")
