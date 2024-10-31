def main():
    n, m = int(input()), int(input())
    flag = True
    k = 1
    for i in range(1, n + 1):
        if flag:
            for j in range(k, m * i + 1):
                print(f'{j:{len(str(m * n))}}', end=' ')
                k = j
            flag = False
            print()
        elif not flag:
            for j in range(m * i, k, -1):
                print(f'{j:{len(str(m * n))}}', end=' ')
            flag = True
            k = m * i + 1
            print()

if __name__ == '__main__':
    main()