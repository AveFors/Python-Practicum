def main():
    a = input().split()
    b = []
    while len(a) != 0:
        value = a.pop(0)
        if value.strip('-').isdigit():
            b.append(int(value))
        match value:
            case '+':
                b.append(int(b.pop()) + int(b.pop()))
            case '-':
                b.append(int(b.pop(-2)) - int(b.pop()))
            case '/':
                b.append(int(b.pop(-2)) // int(b.pop()))
            case '*':
                b.append(int(b.pop()) * int(b.pop()))
            case '~':
                b[-1] = -b[-1]
            case '!':
                res = 1
                for i in range(1, b[-1] + 1):
                    res *= i
                else:
                    b[-1] = res
            case '#':
                b.append(b[-1])
            case '@':
                b[-1], b[-2], b[-3] = b[-3], b[-1], b[-2]
    print(*b)


if __name__ == '__main__':
    main()
