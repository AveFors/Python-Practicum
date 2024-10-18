def main():
    n = int(input())
    k = int(input())
    if n < k:
        for i in range(n, k + 1):
            print(i, end=' ')
    else:
        for i in range(n, k - 1, -1):
            print(i, end=' ')


if __name__ == '__main__':
    main()