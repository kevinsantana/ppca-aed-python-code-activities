def solve():
    s = []
    balanced = True
    index = 0
    input_string = input()
    while index < len(input_string) and balanced:
        token = input_string[index]
        if token == "(":
            s.append(token)
        elif token == ")":
            if len(s) == 0:
                balanced = False
            else:
                s.pop()

        index += 1

    return balanced and len(s) == 0


if __name__ == "__main__":
    print(solve())
