def main():
    n = int(input())
    a = [input() for i in range(n)]
    res = ''
    for i in a:
        mx = 0
        for j in i:
            if mx < int(j):
                mx = int(j)
        res += str(mx)
    print(res)


if __name__ == '__main__':
    main()