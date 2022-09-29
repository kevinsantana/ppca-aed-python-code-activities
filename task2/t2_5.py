def solve():
    sequence = input()
    while True:
        if "()" in sequence:
            sequence = sequence.replace("()", "")
        elif "{}" in sequence:
            sequence = sequence.replace("{}", "")
        elif "[]" in sequence:
            sequence = sequence.replace("[]", "")
        else:
            return not sequence


if __name__ == "__main__":
    print(solve())
