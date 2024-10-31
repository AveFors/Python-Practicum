def main():
    n, m = int(input()), int(input())
    count_m = 0
    for i in range(1, n * m + 1):
        print(f'{i:{len(str(n * m))}}', end=' ')
        count_m += 1
        if count_m == m:
            count_m = 0
            print()

if __name__ == '__main__':
    main()