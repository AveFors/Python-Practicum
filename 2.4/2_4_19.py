def main():
    n = int(input())
    for x in range(n):
        for y in range(n):
            mns = min(x, y, n - x - 1, n - y - 1) + 1
            print(f'{mns:{len(str((n + 1) // 2))}}', end=' ')
        print()

if __name__ == '__main__':
    main()