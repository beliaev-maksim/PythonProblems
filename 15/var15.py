import math
import random
import cProfile


def main():
    try:
        x = float(input("X of main point:\t"))
        y = float(input("Y of main point:\t"))
    except ValueError:
        return print("Value is not a number. Exit")

    main_point = [x, y]

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
                               random.randint(0, 100)])

    print(list_of_points)

    relative_points = []
    for point in list_of_points:
        relative_points.append([point[0] - main_point[0],
                                point[1] - main_point[1]])

    ang_x = 1e9
    point1 = None
    point2 = None
    for i, elem in enumerate(relative_points):
        for j in range(i + 1, num_points):
            # calculate length between two points
            ab = elem[0]*relative_points[j][0] + elem[1]*relative_points[j][1]
            a = math.sqrt(elem[0]**2 + elem[1]**2)
            b = math.sqrt(relative_points[j][0]**2 + relative_points[j][1]**2)
            ang = math.acos(ab/(a*b))

            if ang < ang_x:
                ang_x = ang
                point1 = list_of_points[i]
                point2 = list_of_points[j]

    ang_deg = math.degrees(ang_x)
    print("Smallest angle:\t", ang_deg)
    print("Between {} and {}".format(point1, point2))


if __name__ == "__main__":
    cProfile.run("main()")
