def main():
    n, m = int(input()), int(input())
    k = 0
    for i in range(n):
        for j in range(i + 1, m * n + 1, n):
            k += 1
            print(f'{j:{len(str(m * n))}}', end=' ')
            if k % m == 0:
                print()

if __name__ == '__main__':
    main()