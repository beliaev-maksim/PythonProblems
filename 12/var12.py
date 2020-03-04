import math
import random
import cProfile


def main():
    try:
        x = float(input("X of main point:\t"))
        y = float(input("Y of main point:\t"))
        radius_main = float(input("Radius of main circle:\t"))
    except ValueError:
        return print("Value is not a number. Exit")

    main_point = [x, y]

    try:
        num_points = int(input("Number of points, should be greater or equal than 10:\t"))
    except ValueError:
        return print("Value is not an integer. Exit")

    if num_points < 10:
        return print("Number of points should be greater than 10. Exit")

    # generate random 2D coordinates, integers and limit by 100
    list_of_points = []
    list_of_radius = []
    for i in range(num_points):
        list_of_points.append([random.randint(0, 100),
                               random.randint(0, 100)])

        list_of_radius.append(random.randint(1, 50))

    print(list_of_points)

    for i, point in enumerate(list_of_points):
        vec_1 = math.sqrt((main_point[0] - point[0]) ** 2 +
                          (main_point[1] - point[1]) ** 2)

        if list_of_radius[i] + radius_main >= vec_1:
            print("index:\t", i,
                  "point:\t", point,
                  "radius:\t", list_of_radius[i])


if __name__ == "__main__":
    cProfile.run("main()")
