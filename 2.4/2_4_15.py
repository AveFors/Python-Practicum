def main():
    n, m = int(input()), int(input())
    for i in range(n):
        for j in range(m):
            if j % 2 == 0:
                print(f'{i + j * n + 1:{len(str(m * n))}}', end=' ')
            else:
                print(f'{(j + 1) * n - i:{len(str(m * n))}}', end=' ')
        print()

if __name__ == '__main__':
    main()