def main():
    count = 0
    n = int(input())
    res = 0
    for i in range(n):
        while (k := input()) != 'ВСЁ':
            if k == 'зайка':
                count += 1
        else:
            if count > 1:
                res += 1
            else:
                res += count
            count = 0
    print(res)


if __name__ == '__main__':
    main()