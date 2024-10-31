def main():
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=' ')
        print('\n', end='')


if __name__ == '__main__':
    main()