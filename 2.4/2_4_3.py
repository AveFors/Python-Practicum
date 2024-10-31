def main():
    n = int(input())
    k = 1
    b = 1
    while b <= n:
        for i in range(1, k + 1):
            print(b, end=' ')
            b += 1
            if b > n:
                break
        k += 1
        print('\n', end='')


if __name__ == '__main__':
    main()