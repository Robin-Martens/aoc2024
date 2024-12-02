def parse_input(filename: str) -> list[list[int]]:
    lst: list[list[int]] = []
    with open(filename, "r") as f:
        for line in f.readlines():
            lst.append([int(n) for n in line.split(" ")])
        return lst


def is_safe(report: list[int]) -> bool:
    if report in [sorted(report, reverse=r) for r in [True, False]]:
        differences = [abs(x - report[i - 1]) for i, x in enumerate(report)][1:]
        return sum([differences.count(i) for i in range(1, 4)]) == len(differences)
    return False


def remove_occ(report: list[int], elem: int, occ: int) -> list[int]:
    new_report = []
    elem_visited = 0
    for item in report:
        if elem == item:
            elem_visited += 1

            if elem_visited != occ:
                new_report.append(item)
        else:
            new_report.append(item)
    return new_report


def part1(data: list[list[int]]) -> int:
    return sum([is_safe(report) for report in data])


def part2(data: list[list[int]]) -> int:
    counter = 0
    for report in data:
        if is_safe(report):
            counter += 1
        else:
            n_dict = {}
            is_saf = False
            for n in report:
                if n not in n_dict.keys():
                    n_dict[n] = 1
                else:
                    n_dict[n] += 1

                new_lst = remove_occ(report, n, n_dict[n])
                if is_safe(new_lst) and not is_saf:
                    counter += 1
                    is_saf = True
    return counter


if __name__ == "__main__":
    test_data = parse_input("./input_test")
    data = parse_input("./input")

    assert part1(test_data) == 2
    print(part1(data))

    assert part2(test_data) == 4
    print(part2(data))
