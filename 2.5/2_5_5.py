def main():
    n = int(input())
    b = [[] for i in range(n)]
    for i in range(n):
        while (k := input()) != 'end':
            b[i].append(int(k))
    mx = 10 ** 9
    for i in range(len(b)):
        mx = min(mx, (sum(b[i]) / len(b[i])))
    print(round(mx, 2))


if __name__ == '__main__':
    main()
