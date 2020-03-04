import cProfile
import json

with open("D:\\1.txt", "r") as file:
    seq = json.load(file)["seq"]


def main():
    # 2.481
    flag_zero = False
    counter = 0
    sub_ind = 0
    for i, elem in enumerate(seq):
        if elem == 0:
            if flag_zero:
                counter += sub_ind
            else:
                flag_zero = True

            sub_seq = []
            sub_ind = 0
            continue

        if flag_zero:
            sub_seq.append(elem)
            sub_ind += i

    if counter > 0:
        print(counter)
    else:
        print("No 2 zeros")


if __name__ == "__main__":
    cProfile.run("main()")
