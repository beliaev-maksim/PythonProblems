import cProfile
import json

with open("D:\\1.txt", "r") as file:
    seq = json.load(file)["seq"]


def main():
    # 2.993s
    num_points = len(seq)
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
            n1 = j+1

    print(sum_val)


if __name__ == "__main__":
    cProfile.run("main()")
