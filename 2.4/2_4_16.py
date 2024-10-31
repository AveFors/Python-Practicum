def main():
    n, m = int(input()), int(input())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{i * j:^{m}}', end='|' if j != n else '')
        print()
        if i != n:
            print('-' * (n * (m + 1) - 1))

if __name__ == '__main__':
    main()