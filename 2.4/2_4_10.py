def main():
    n = int(input())
    print('А Б В')
    for i in range(1, n - 1):
        for j in range(1, n - i):
            for k in range(1, n - j):
                if i + j + k == n:
                    print(i, j, k)

if __name__ == '__main__':
    main()