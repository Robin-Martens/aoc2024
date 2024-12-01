def parse_input(filename: str) -> tuple[list[int], list[int]]:
    l1: list[int] = []
    l2: list[int] = []
    with open(filename, "r") as f:
        for line in f.readlines():
            n1, n2 = [int(n) for n in line.split("   ")]
            l1.append(n1)
            l2.append(n2)

        return (l1, l2)

def main(input_: tuple[list[int], list[int]]) -> int:
    l1, l2 = input_




if __name__ == "__main__":
    input_ = parse_input("input_test")

