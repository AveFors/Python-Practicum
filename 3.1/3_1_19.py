def main():
    a = input().split()
    i = 0
    while len(a) != 1:
        if a[i] == '*':
            a[i] = int(a[i - 1]) * int(a[i - 2])
            a.pop(i - 1)
            a.pop(i - 2)
            i -= 2
        elif a[i] == '+':
            a[i] = int(a[i - 2]) + int(a[i - 1])
            a.pop(i - 1)
            a.pop(i - 2)
            i -= 2
        elif a[i] == '-':
            a[i] = int(a[i - 2]) - int(a[i - 1])
            a.pop(i - 1)
            a.pop(i - 2)
            i -= 2
        i += 1
    print(*a)


if __name__ == '__main__':
    main()
