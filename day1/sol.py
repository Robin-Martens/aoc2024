import numpy as np


def parse_input(filename: str) -> tuple[list[int], list[int]]:
    l1: list[int] = []
    l2: list[int] = []
    with open(filename, "r") as f:
        for line in f.readlines():
            n1, n2 = [int(n) for n in line.split("   ")]
            l1.append(n1)
            l2.append(n2)

        return (l1, l2)


def part1(input_: tuple[list[int], list[int]]) -> int:
    l1, l2 = input_

    l1 = np.array(l1)
    l2 = np.array(l2)

    return np.sum(np.abs(np.sort(l1) - np.sort(l2)))


def part2(input_: tuple[list[int], list[int]]) -> int:
    l1, l2 = input_

    l1 = np.array(l1)
    l2 = np.array(l2)

    counts = [np.sum(l2 == n) for n in l1]

    return sum(l1 * counts)


if __name__ == "__main__":
    input_test = parse_input("input_test")
    assert part1(input_test) == 11
    assert part2(input_test) == 31

    print(part1(parse_input("input")))
    print(part2(parse_input("input")))
