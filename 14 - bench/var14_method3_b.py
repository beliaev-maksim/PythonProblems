import cProfile
import json

with open("D:\\1.txt", "r") as file:
    seq = json.load(file)["seq"]

def main():
    # 2.774
    counter = 0
    sub_ind = 0
    sub_seq = []

    try:
        i = seq.index(0)
    except ValueError:
        return print("No zeros")

    for j, elem in enumerate(seq[i:]):
        if elem == 0:
            counter += sub_ind
            sub_seq = []
            sub_ind = 0
            continue

        sub_seq.append(elem)
        sub_ind += j + i

    if counter > 0:
        print(counter)
    else:
        print("No 2 zeros")


if __name__ == "__main__":
    cProfile.run("main()")
