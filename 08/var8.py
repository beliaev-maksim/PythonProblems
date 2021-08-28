import cProfile
import random

DIMENSION = 20
PRIME_NUMBER_LIST = [2, 3, 5, 7, 11, 13, 17, 19]


def main():
    check_list = []
    for i in range(DIMENSION):
        check_list.append(random.randint(1, 20))

    # try:
    #     seq = input("Type sequence of number 1-20, comma separated.:\t")
    #     check_list = [int(elem) for elem in seq.split(",")]
    # except ValueError:
    #     return print("Value is not a number. Exit")
    #
    # # this loop may be combined but for readability we will use separate one
    # for elem in check_list:
    #     if not 1 <= elem <= 20:
    #         return print("All points should be in range 1-20. Exit")

    primes = []
    non_primes = []
    for elem in check_list:
        if elem in PRIME_NUMBER_LIST:
            primes.append(elem)
        else:
            non_primes.append(elem)

    print("Number of prime numbers:\t", len(primes))
    print("Prime numbers:\t", sorted(primes)[::-1])
    print("Non-Prime numbers:\t", sorted(non_primes))


if __name__ == "__main__":
    cProfile.run("main()")