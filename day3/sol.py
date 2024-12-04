import re

def read_data(filename: str) -> str:
    with open(filename, "r") as f:
        return "".join([line for line in f.readlines()])

def calc(mul_str: str) -> int:
    raw = mul_str.replace('mul(', '').replace(')', '')
    n1, n2 = raw.split(',')
    return int(n1) * int(n2)

def part1(data: str) -> int:
    rg = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    matches = [match.group() for match in rg.finditer(data)]
    return sum([calc(s) for s in matches])

def in_intervals(idx: int, ranges: list[tuple[int, int]]) -> bool:
    for ran in ranges:
        if ran[0] <= idx <= ran[1]:
            return True
    return False

def find_next_dont(idx: int, data: list[tuple[int, bool]]) -> int:
    for d in data[idx:]:
        if not d[1]:
            return d[0]
    return -1

def create_ranges(data: list[tuple[int, bool]]) -> list[tuple[int, int]]:
    ranges = []
    for i in range(len(data)):
        if data[i][1]:
            next_dont = find_next_dont(i, data)
            if next_dont != -1:
                ranges.append((data[i][0], next_dont))
    return ranges

def part2(data: str) -> int:
    rg = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    rg_do = re.compile(r"do\(\)")
    rg_dont = re.compile(r"don't\(\)")

    matches = [(m.span()[0], m.group()) for m in rg.finditer(data)]
    matches_do = [0] + [m.span()[0] for m in rg_do.finditer(data)]
    matches_dont = [m.span()[0] for m in rg_dont.finditer(data)] + [max(matches, key=lambda item: item[0])[0] + 1]

    do_counter = 1
    dont_counter = 0
    combined = [(0, True)]
    while do_counter < len(matches_do) and dont_counter < len(matches_dont):
        do = matches_do[do_counter]
        dont = matches_dont[dont_counter]

        if dont < do and dont > combined[-1][0]:
            combined.append((dont, False))
            dont_counter += 1
        elif combined[-1][0] < do and do < dont:
            combined.append((do, True))
            do_counter+= 1

    if do_counter < len(matches_do):
        combined += [(idx, True) for idx in matches_do[do_counter:]]
    if dont_counter < len(matches_dont):
        combined += [(idx, False) for idx in matches_dont[dont_counter:]]

    sum = 0
    for i, m in matches:
        if in_intervals(i, create_ranges(combined)):
            sum += calc(m)
    return sum



if __name__ == "__main__":
    test_data = read_data("./input_test")
    data = read_data("./input")

    assert part1(test_data) == 161
    print(part1(data))

    test_data2 = read_data("./input_test2")
    assert part2(test_data2) == 48
    print(part2(data))



